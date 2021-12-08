from ..memory.replay_memory import ReplayMemory
from ..utils import identity
from abc import abstractmethod
import torch as th
import numpy as np
import gym
import sys


class Agent(object):
    """
    A unified agents interface:
    - interact: interact with the environment to collect experience
        - _take_one_step: take one step
        - _take_n_steps: take n steps
        - _discount_reward: discount roll out rewards
    - train: train on a sample batch
        - _soft_update_target1: soft update the target network
    - exploration_action: choose an action based on state with random noise
                            added for exploration in training
    - action: choose an action based on state for execution
    - value: evaluate value for a state-action pair
    - evaluation: evaluation a learned agents
    """

    def __init__(self, env: gym.wrappers.time_limit.TimeLimit, state_dim: int, action_dim: int,
                 memory_capacity=10000, max_steps=10000,
                 reward_gamma=0.99, reward_scale=1., done_penalty=None,
                 actor_hidden_size=32, critic_hidden_size=32,
                 actor_output_act=identity, critic_loss="mse",
                 actor_lr=0.01, critic_lr=0.01,
                 optimizer_type="rmsprop", entropy_reg=0.01,
                 max_grad_norm=0.5, batch_size=100, episodes_before_train=100,
                 epsilon_start=0.9, epsilon_end=0.01, epsilon_decay=200,
                 use_cuda=True):

        self.env: gym.Env = env
        self.state_dim: int = state_dim
        self.action_dim: int = action_dim
        self.env_state: np.ndarray = self.env.reset()  # get  state zero of env
        self.n_episodes: int = 0
        self.n_steps: int = 0
        self.max_steps: int = max_steps
        self.roll_out_n_steps: int = 1

        self.reward_gamma: float = reward_gamma
        self.reward_scale: float = reward_scale
        self.done_penalty: float = done_penalty

        self.memory: ReplayMemory = ReplayMemory(memory_capacity)
        self.actor_hidden_size: int = actor_hidden_size
        self.critic_hidden_size: int = critic_hidden_size
        self.actor_output_act: int = actor_output_act
        self.critic_loss: str = critic_loss
        self.actor_lr: float = actor_lr
        self.critic_lr: float = critic_lr
        self.optimizer_type: str = optimizer_type
        self.entropy_reg: float = entropy_reg
        self.max_grad_norm: float = max_grad_norm
        self.batch_size: int = batch_size
        self.episodes_before_train: int = episodes_before_train
        self.target_tau: float = 0.01

        # params for epsilon greedy
        self.epsilon_start: float = epsilon_start
        self.epsilon_end: float = epsilon_end
        self.epsilon_decay: float = epsilon_decay

        self.use_cuda = use_cuda and th.cuda.is_available()

    # agents interact with the environment to collect experience
    def interact(self):
        pass
        # NotImplementedError

    # take one step in env
    def _take_one_step(self):
        # if (self.max_steps is not None) and (self.n_steps >= self.max_steps):
        #     self.env_state = self.env.reset()
        #     self.n_steps = 0
        state = self.env_state
        action = self.exploration_action(self.env_state)
        next_state, reward, done, _ = self.env.step(action)

        # sys.stdout.write(
        #     'state:' + str(state) + ', \
        #      next_state:' + str(next_state) + ', \
        #      reward:' + str(reward) + ', \
        #      action:' + str(action) + ', \
        #      n_steps:' + str(self.n_steps) + ' \n'
        # )

        if done or ((self.max_steps is not None) and (self.n_steps >= self.max_steps)):
            if self.done_penalty is not None:
                reward = self.done_penalty
            next_state = [0] * len(state)
            self.n_steps = 0
            self.env_state = self.env.reset()
            self.n_episodes += 1
            self.episode_done = True
        else:
            self.env_state = next_state
            self.episode_done = False
        self.n_steps += 1
        self.memory.push(state, action, reward, next_state, done)

    # take n steps
    def _take_n_steps(self):
        if (self.max_steps is not None) and (self.n_steps >= self.max_steps):
            self.env_state = self.env.reset()
            self.n_steps = 0
        states = []
        actions = []
        rewards = []
        # take n steps
        for i in range(self.roll_out_n_steps):
            states.append(self.env_state)
            action = self.exploration_action(self.env_state)
            next_state, reward, done, _ = self.env.step(action)
            actions.append(action)
            if done and self.done_penalty is not None:
                reward = self.done_penalty
            rewards.append(reward)
            final_state = next_state
            self.env_state = next_state
            if done:
                self.env_state = self.env.reset()
                break
        # discount reward
        if done:
            final_value = 0.0
            self.n_episodes += 1
            self.episode_done = True
        else:
            self.episode_done = False
            final_action = self.action(final_state)
            final_value = self.value(final_state, final_action)
        rewards = self._discount_reward(rewards, final_value)
        self.n_steps += 1
        self.memory.push(states, actions, rewards)

    # discount roll out rewards
    def _discount_reward(self, rewards, final_value):
        discounted_r = np.zeros_like(rewards)
        running_add = final_value
        for t in reversed(range(0, len(rewards))):
            running_add = running_add * self.reward_gamma + rewards[t]
            discounted_r[t] = running_add
        return discounted_r

    # soft update the actor target network or critic target network
    def _soft_update_target(self, target, source):
        for t, s in zip(target.parameters(), source.parameters()):
            t.data.copy_(
                (1. - self.target_tau) * t.data + self.target_tau * s.data)

    # train on a sample batch
    def train(self):
        NotImplementedError("Sub Class Have To Implement This Method")

    # choose an action based on state with random noise added for exploration in training
    def exploration_action(self, state):
        NotImplementedError("Sub Class Have To Implement This Method")

    # choose an action based on state for execution
    def action(self, state):
        NotImplementedError("Sub Class Have To Implement This Method")

    # evaluate value for a state-action pair
    def value(self, state, action):
        NotImplementedError("Sub Class Have To Implement This Method")

    # evaluation the learned agents
    def evaluation(self, env, eval_episodes=10):
        rewards = []
        infos = []
        for i in range(eval_episodes):
            rewards_i = []
            infos_i = []
            state = env.reset()
            action = self.action(state)
            state, reward, done, info = env.step(action)
            done = done[0] if isinstance(done, list) else done
            rewards_i.append(reward)
            infos_i.append(info)
            while not done:
                action = self.action(state)
                state, reward, done, info = env.step(action)
                done = done[0] if isinstance(done, list) else done
                rewards_i.append(reward)
                infos_i.append(info)
            rewards.append(rewards_i)
            infos.append(infos_i)
        return rewards, infos
