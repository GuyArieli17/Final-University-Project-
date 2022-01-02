from simple.replay_memory import ReplayMemory, Experience
from abc import abstractmethod
import torch as th
import numpy as np


class Actor:
    """
        EXPRESS
    """
    def __init__(self, memory_size, network, env, epsilon_start, epsilon_end,
                 action_dim, epsilon_decay, loss_fnc, actor_optimizer, gamma,max_steps,done_penalty,batch_size):
        self.memory = ReplayMemory(memory_size)
        self.network = network
        self.env = env
        self.epsilon_start = epsilon_start
        self.epsilon_end = epsilon_end
        self.epsilon_decay = epsilon_decay
        self.action_dim = action_dim
        self.loss_function = loss_fnc
        self.actor_optimizer = actor_optimizer
        self.gamma = gamma
        self.current_state = env.reset()
        self.n_steps = 1
        self.max_steps = max_steps
        self.done_penalty = done_penalty
        self.n_episodes = 0
        self.batch_size = batch_size

    # run actor inside the environment
    @abstractmethod
    def train(self):
        NotImplementedError("Need to Implement In Sub Class")

    # do only steps don't learn(eval)
    @abstractmethod
    def interact(self):
        NotImplementedError("Need to Implement In Sub Class")

    # choose an action based on state with random noise added for exploration in training
    def _exploration_action(self, state):
        epsilon = self.epsilon_end + (self.epsilon_start - self.epsilon_end) * \
                  np.exp(-1. * self.n_steps / self.epsilon_decay)
        if np.random.rand() < epsilon:
            rnd_action = np.random.choice(self.action_dim)
            return rnd_action
        learned_action = th.argmax(self.network(th.tensor(state).float()))
        return learned_action

    # do one step in world (without train do one step and push to memory)
    def _take_one_step(self):
        state = self.current_state
        action = self._exploration_action(self.current_state)
        next_state, reward, done, _ = self.env.step(action)
        if done and (self.n_steps >= self.max_steps):
            reward = self.done_penalty
            next_state = np.zeros(len(state))
            self.n_steps = 0
            self.current_state = self.env.reset()
            self.n_episodes += 1
            self.episode_done = True
        else:
            self.current_state = next_state
            self.episode_done = False
        self.n_steps += 1
        self.memory.push(state, action, reward, next_state, done)


class DQN(Actor):
    """
        EXPRESS
    """
    def __init__(self, memory_size, network, env, epsilon_start, epsilon_end,
                 action_dim, epsilon_decay, loss_fnc, actor_optimizer, gamma, max_steps, done_penalty, batch_size):
        super(DQN, self).__init__(memory_size, network, env, epsilon_start, epsilon_end, action_dim, epsilon_decay,
                                  loss_fnc, actor_optimizer, gamma, max_steps, done_penalty, batch_size)

    # do interaction with the world (insert to memory)
    def interact(self):
        super(DQN, self)._take_one_step()

    # do a train to the network with random bath from memory
    def _train_mini_batch(self, mini_batch):
        # Todo: Add examples
        done_tensor = th.zeros(*mini_batch.shape[:-1])
        reward_tensor = th.zeros(*mini_batch.shape[:-1])
        current_states_tensor = th.zeros((*mini_batch.shape[:-1], *self.current_state.shape))
        next_states_tensor = th.zeros((*mini_batch.shape[:-1], *self.current_state.shape))
        for idx, exp in enumerate(mini_batch):
            exp_state, exp_action, exp_reward, exp_new_state, exp_done = list(
                    map(lambda val: th.tensor(val).float(), [*exp]))
            done_tensor[idx] = exp_done
            current_states_tensor[idx] = exp_state
            reward_tensor[idx] = exp_reward
            next_states_tensor[idx] = exp_new_state
        prediction = self.network(current_states_tensor)
        prediction_next = self.network(next_states_tensor)
        # get the index of the best action(in last position)
        best_action_indexes = th.argmax(prediction, dim=-1)
        best_action_indexes_next = th.argmax(prediction_next, dim=-1)
        # select for each state best q-value
        current_state_predictions = prediction[:, :, best_action_indexes]
        current_state_predictions_next = prediction_next[:, :, best_action_indexes_next]
        # create RL labels
        # TOdo: add zero gradient
        labels = reward_tensor + th.logical_not(done_tensor) * (self.gamma * current_state_predictions_next)
        loss = self.loss_function(labels, current_state_predictions)
        loss.backward()
        self.actor_optimizer.step()

    # make a step and train network
    def train(self):
        action = self._exploration_action([self.current_state])
        current_state = self.current_state
        new_state, reward, done, _ = self.env.step(action)
        # change to tensor type
        new_state = th.tensor(new_state).float()
        reward = th.tensor(reward).float()
        done = th.tensor(done).float()
        # append to buffer memory
        self.memory.push(current_state, th.tensor(action).float(), reward, new_state, done)
        # choose randomly n size batch
        mini_batch = self.memory.sample(self.batch_size)
        mini_batch = np.array(mini_batch)
        # train the batch
        self._train_mini_batch(mini_batch)










