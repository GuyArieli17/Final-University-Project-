# ==================================================================================
#       Copyright (c) 2019-2022 Guy Arieli (GuyArieli17)
#       Copyright (c) 2018-2020 Eran
#       Copyright (c) 2018-2020 Amit
#
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
# ==================================================================================

import gym
from gym import spaces
import numpy as np
from .cityflow_api import CityFlowAPI

"""
    This class Environment,
    The env present all the action we can do.
    according to gym.ENV API DOC: https://gym.openai.com/docs/
"""
class Environment(gym.Env):

    ###############
    # PRIVATE API #
    ###############

    _COOL_DOWN_IN_STEPS = 7
    _MIN_ACTION_STEPS = 3
    _RED_LIGHT_ACTION = 8

    # class constructor
    def __init__(self, state_func: callable(dict), reward_func: callable((np.array, np.array)),
                 action_space: spaces.Discrete, observation_space: spaces.Box,
                 reward_range: tuple, config: str) -> None:
        """
            @Parameters
            ----------
            state_func: callable(dict)
                the function will get the state from the CityflowApi and 
                create a state function we will work with

            reward_func: callable((np.array, np.array)
                the function will get the current state,
                the previous state and calc the reward 

            action_space: spaces.Discrete
                this is an object that determine the shape of our 
                action space 

            observation_space: spaces.Box
                this is an object that determine the shape of our 
                state space 
            
            reward_range: tuple
                determine the (max,min) value of 
                reward function 
                
            configh: str
                A relative path to the config file
            ----------

            @Returns
            -----------
            None
            ----------
        """
        # call parent constructor
        super(Environment, self).__init__()
        #save all metadata from argument of the constructor
        self._prev_action = None
        self._state_func: callable = state_func
        self._reward_range: tuple = reward_range
        self._reward_func: callable = reward_func
        self._action_space: spaces.Discrete = action_space
        self._observation_space: spaces.Box = observation_space
        # crete instance of api (for easy acess)
        self._api = CityFlowAPI(config)

    ##############
    # PUBLIC API #
    ##############
    
    # the function will reset the simulation and return the last state
    def reset(self) -> np.array:
        """
            The function will reset the simulation and return the last state

            @Parameters
            ----------
            None
            ----------

            @Returns
            -----------
            State: 
                the last state before the reset
            ----------
        """
        self._api.reset()
        last_state = self._state_func(self._api.state())
        return last_state

    # private function: will frezee all state untill let the simulator get action from user
    def _after_action_cool_down(self, intersection_id = 'intersection_1_1') -> None:
        """
            Will frezee all lights 
            Untill the freeze time is up.
            (
                created to prevent situation where there is a car
                in the intersection, and the other lights will hace
                a green light
            )

            @Parameters
            ----------
                intersection_id: str
                    an id of the intesectio in the config file
            ----------
            @Returns
            -----------
                None
            ----------
        """
        # set all red action in simulation
        self._api.set_action(intersection_id, self._RED_LIGHT_ACTION)
        # wait _COOL_DOWN_IN_STEPS frame untill continue
        for _ in range( self._COOL_DOWN_IN_STEPS):
            self._api.next_frame()
    
    # determine an action in simulation and activate it (next frame)
    def step(self, action: int):
        """
            Get action from user and activate this functio in 
            the simulation return inforamtuion as a tuple

            @Parameters
            ----------
                action: int
                    index of action writtin in the json file 
            ----------
            @Returns
            -----------
                tuple: 
                    all the data we need in gym.env (next_state, reward,done,_)
            ----------
        """
        # in change in lightphase cooldown should be set
        if self._prev_action != action:
            self._after_action_cool_down()

        # get the state before action
        prev_state = self._state_func(self._api.state())
        # activate the action
        self._api.set_action('intersection_1_1', action)
        self._api.next_frame()
        # get the new state
        next_state = self._state_func(self._api.state())
        reward = self._reward_func(prev_state, next_state)
        # save the last preforme action
        self._prev_action = action
        # didnt finish 
        done = False
        return next_state, reward, done, []
