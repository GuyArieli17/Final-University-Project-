import gym
from gym import spaces
import numpy as np


class TrafficSteeringEnvironment(gym.Env):
    # metadata = {'render.modes': ['human']}

    def __init__(self):
        super(TrafficSteeringEnvironment, self).__init__()
        # self.df = df
        # self.reward_range = (0, MAX_ACCOUNT_BALANCE)
        # Actions of the format Buy x%, Sell x%, Hold, etc.
        self.action_space = spaces.Box(
            low=np.array([0]), high=np.array([8]), dtype=np.int64
        )
        print(self.action_space)
        # self.action_space = np.zeros((1, 8))

        # Prices contains the OHCL values for the last five prices
        # self.observation_space = spaces.Box(
        # low=0, high=1, shape=(6, 6), dtype=np.float16)
        self.observation_space = spaces.Box(
            low=0, high=1, shape=(6, 6), dtype=np.float16
        )

        # self.action_space = None
        # self.observation_space = None


t = TrafficSteeringEnvironment()
