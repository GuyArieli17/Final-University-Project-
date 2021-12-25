from simple.models import *
from simulation.environment import TrafficSteeringEnvironment
from reward_func import *
from state_parser import *
from gym import spaces
import numpy as np
from simple.actors import DQN
import sys
import torch as th
from torch import nn
from torch import optim

EPISODES_BEFORE_TRAIN = 0
EVAL_EPISODES = 0
EVAL_INTERVAL = 1
# max steps in each episode, prevent from running too long
MEMORY_CAPACITY = 100
BATCH_SIZE = 100
CRITIC_LOSS = "mse"
MAX_GRAD_NORM = None
REWARD_DISCOUNTED_GAMMA = 0.99
EPSILON_START = 0.99
EPSILON_END = 0.05
EPSILON_DECAY = 50
RANDOM_SEED = 2017
ACTION_DIM = 8
STATE_DIM = 24
HIDDEN_LAYER = 50
sys.stdout.write('start\n')
ACTION_SPACE = spaces.Box(
    low=np.array([0]),  # Lower bound
    high=np.array([8]),  # Upper bound
    dtype=np.int64)
REWARD_RANGE = (-np.inf, np.inf)

#  Things i might change
OBSERVATION_SPACE = spaces.Box(
    low=np.array([-np.inf for _ in range(STATE_DIM)]),  # Lower bound
    high=np.array([np.inf for _ in range(STATE_DIM)]),  # Upper bound
    dtype=np.int64)
STATE_FUNC = state_of_waiting_cars
REWARD_FUNC = reward_of_waiting_cars
# MODEL = ActorNetwork(STATE_DIM, HIDDEN_LAYER, ACTION_DIM, nn.ReLU())
MODEL = RecurrentNeuralNetwork(STATE_DIM, HIDDEN_LAYER, 10, ACTION_DIM, nn.ReLU(), BATCH_SIZE)
LOSS_FUNCTION = nn.MSELoss()
OPTIMIZE = optim.Adam(MODEL.parameters())
MAX_STEPS = 250
MAX_EPISODES = 1
DONE_PENALTY = -10.


if __name__ == "__main__":
    sys.stdout.write('main\n')
    for param in MODEL.parameters():
        param.requires_grad = True
    env = TrafficSteeringEnvironment(state_func=STATE_FUNC, reward_func=REWARD_FUNC, action_space=ACTION_SPACE,
                                     observation_space=OBSERVATION_SPACE, reward_range=REWARD_RANGE)
    actor = DQN(memory_size=5, network=MODEL, env=env, epsilon_start=EPSILON_START, epsilon_end=EPSILON_END,
                action_dim=ACTION_DIM, epsilon_decay=EPSILON_DECAY, loss_fnc=LOSS_FUNCTION, actor_optimizer=OPTIMIZE,
                gamma=REWARD_DISCOUNTED_GAMMA, max_steps=MAX_STEPS, done_penalty=DONE_PENALTY, batch_size=BATCH_SIZE)
    print(MODEL)
    total_step = 0
    done = False
    for ep_idx in range(MAX_EPISODES):
        for stp_idx in range(MAX_STEPS):
            actor.train()
            done = total_step > 10
            if done:
                break
        if done:
            break
