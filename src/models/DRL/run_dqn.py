
from DQN import DQN
from common.utils import agg_double_list

import os
import sys
import time
# import gym
import numpy as np
# import matplotlib.pyplot as plt

from mediator.custom_enviroment import TrafficSteeringEnvironment


# MAX_EPISODES = 5_000
MAX_EPISODES = 5
EPISODES_BEFORE_TRAIN = 0
EVAL_EPISODES = 10
EVAL_INTERVAL = 1

# max steps in each episode, prevent from running too long
# MAX_STEPS = 10_000  # None
MAX_STEPS = 100  # None

MEMORY_CAPACITY = 10_000
BATCH_SIZE = 100
CRITIC_LOSS = "mse"
MAX_GRAD_NORM = None

REWARD_DISCOUNTED_GAMMA = 0.99

EPSILON_START = 0.99
EPSILON_END = 0.05
EPSILON_DECAY = 50

DONE_PENALTY = -10.

RANDOM_SEED = 2017

sys.stdout.write('start\n')


def run(env_class):
    env = env_class()
    env.seed(RANDOM_SEED)

    env_eval = env_class()
    env_eval.seed(RANDOM_SEED)

    state_dim: int = env.observation_space.shape[0]
    if len(env.action_space.shape) >= 1:
        action_dim = env.action_space.shape[0]
    else:
        action_dim = env.action_space.n

    dqn = DQN(env=env, memory_capacity=MEMORY_CAPACITY,
              state_dim=state_dim, action_dim=action_dim,
              batch_size=BATCH_SIZE, max_steps=MAX_STEPS,
              done_penalty=DONE_PENALTY, critic_loss=CRITIC_LOSS,
              reward_gamma=REWARD_DISCOUNTED_GAMMA,
              epsilon_start=EPSILON_START, epsilon_end=EPSILON_END,
              epsilon_decay=EPSILON_DECAY, max_grad_norm=MAX_GRAD_NORM,
              episodes_before_train=EPISODES_BEFORE_TRAIN)

    episodes = []
    eval_rewards = []

    sys.stdout.write('start EPISODES\n')

    while dqn.n_episodes < MAX_EPISODES:
        sys.stdout.write('episode: ' + str(dqn.n_episodes)+ ', n_steps: ' + str(dqn.n_steps) + '\n')
        dqn.interact()
        if dqn.n_episodes >= EPISODES_BEFORE_TRAIN:
            dqn.train()
        if dqn.episode_done and ((dqn.n_episodes+1) % EVAL_INTERVAL == 0):
            # sys.stdout.write('eval ' + str(dqn.n_episodes)+'\n')
            # rewards, _ = dqn.evaluation(env_eval, EVAL_EPISODES)
            # rewards_mu, rewards_std = agg_double_list(rewards)
            # sys.stdout.write("Episode %d, Average Reward %.2f" %
            #                  (dqn.n_episodes+1, rewards_mu))
            episodes.append(dqn.n_episodes+1)
            # eval_rewards.append(rewards_mu)

    sys.stdout.write('done EPISODES\n')

    episodes = np.array(episodes)
    eval_rewards = np.array(eval_rewards)
    np.savetxt("./container-output/%s_dqn_episodes.txt" %
               "TrafficSteeringEnvironment", episodes)
    np.savetxt("./container-output/%s_dqn_eval_rewards.txt" %
               "TrafficSteeringEnvironment", eval_rewards)

    sys.stdout.write('done saves\n')

    # time.sleep(5000)

    # plt.figure()
    # plt.plot(episodes, eval_rewards)
    # plt.title("%s" % env_id)
    # plt.xlabel("Episode")
    # plt.ylabel("Average Reward")
    # plt.legend(["DQN"])
    # plt.savefig("./output/%s_dqn.png" % env_id)


if __name__ == "__main__":
    sys.stdout.write('main\n')
    run(TrafficSteeringEnvironment)
