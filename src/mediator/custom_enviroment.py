import os
import gym
from gym import spaces
import numpy as np
from dotenv import load_dotenv
from mediator.API import Cityflow_API

load_dotenv()


class TrafficSteeringEnvironment(gym.Env):
    # metadata = {'render.modes': ['human']}

    def __init__(self):
        super(TrafficSteeringEnvironment, self).__init__()

        # [lightphase]
        self.action_space = spaces.Box(
            low=np.array([0]), high=np.array([7]), dtype=np.int64
        )

        # [count_vehicle_waiting]
        self.observation_space = spaces.Box(
            low=np.array([0]), high=np.array([np.inf]), dtype=np.int64
        )

        self.reward_range = (-np.inf, np.inf)

        self.api = Cityflow_API(os.getenv("CONFIG_JSON_FILE"))

    def reset(self):
        self.api.reset()
        return self.api.get_state()

    def step(self, action):
        prev_state = self.api.get_state()

        self.api.set_action('intersection_1_1', action[0])
        self.api.next_frame()

        next_state = self.api.get_state()
        reward = prev_state[0] - next_state[0]
        done = False

        return next_state, reward, done, []

    # def render(self, mode="human"):
        # pass


t = TrafficSteeringEnvironment()
