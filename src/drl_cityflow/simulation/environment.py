import os
import gym
from gym import spaces
import numpy as np
from dotenv import load_dotenv
from simulation.api import CityFlowAPI

load_dotenv()
COOL_DOWN_IN_STEPS = 7
MIN_ACTION_STEPS = 3
RED_LIGHT_ACTION = 8


class TrafficSteeringEnvironment(gym.Env):
    """This"""

    def __init__(self, state_func: callable(dict), reward_func: callable((np.array, np.array)),
                 action_space: spaces.Discrete, observation_space: spaces.Box,
                 reward_range: tuple) -> None:
        super(TrafficSteeringEnvironment, self).__init__()
        self.prev_action = None
        self.state_func: callable = state_func
        self.reward_range: tuple = reward_range
        self.reward_func: callable = reward_func
        self.action_space: spaces.Discrete = action_space
        self.observation_space: spaces.Box = observation_space
        self.api = CityFlowAPI('./simulation/config/config.json')

    def reset(self):
        """
            Return to start position &
            Return first state
        """
        self.api.reset()
        return self.state_func(self.api.get_state())

    def _after_action_cool_down(self):
        self.api.set_action('intersection_1_1', RED_LIGHT_ACTION)
        for i in range(COOL_DOWN_IN_STEPS):
            self.api.next_frame()

    def step(self, action: int):
        """
            make @param action in env
            and return new state + reward + is finish , _
        """
        if self.prev_action != action:
            self._after_action_cool_down()
        # start
        prev_state = self.state_func(self.api.get_state())
        self.api.set_action('intersection_1_1', action)
        self.api.next_frame()
        next_state = self.state_func(self.api.get_state())
        reward = self.reward_func(prev_state, next_state)
        self.prev_action = action
        done = False
        return next_state, reward, done, []
