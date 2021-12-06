import os
import gym
from gym import spaces
import numpy as np
from dotenv import load_dotenv
from mediator.API import Cityflow_API

load_dotenv()
COOL_DOWN_IN_STEPS = 7
MIN_ACTION_STEPS = 3
RED_LIGHT_ACTION = 8


class TrafficSteeringEnvironment(gym.Env):

    def __init__(self)->None:
        super(TrafficSteeringEnvironment, self).__init__()
        # [lightphase]
        self.action_space = spaces.Discrete(8)
        # [count_vehicle_waiting]
        self.observation_space = spaces.Box(low=np.array([0]), high=np.array([np.inf]), dtype=np.int64)
        # [reward]
        self.reward_range = (-np.inf, np.inf)
        # taking api
        self.api = Cityflow_API(os.getenv("CONFIG_JSON_FILE"))
        self.prev_action = None


    def reset(self):
        """
            Return to start position &
            Return first state
        """
        self.api.reset()
        return self.api.get_state()

    def _after_action_cool_down(self):
        self.api.set_action('intersection_1_1', RED_LIGHT_ACTION)
        for i in range(COOL_DOWN_IN_STEPS):
            self.api.next_frame()

    def step(self, action):
        """
            make @param action in env
            and return new state + reward + is finish , _
        """
        if self.prev_action != action:
            self._after_action_cool_down()
        # start
        prev_state = self.api.get_state()
        self.api.set_action('intersection_1_1', action)
        self.api.next_frame()
        next_state = self.api.get_state()
        reward = prev_state - next_state
        self.prev_action = action
        done = False
        return next_state, reward, done, []
