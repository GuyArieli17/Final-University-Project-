# ==================================================================================
#       Copyright (c) 2019-2022 Guy Arieli (GuyArieli17)
#       Copyright (c) 2018-2020 Eran
#       Copyright (c) 2018-2020 Amit
#
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
# ==================================================================================
import random
from collections import namedtuple
import numpy as np

# a tuplename (enum tuple in rust)
# that hold experience struct {
#   state,
#   action,
#   reward,
#   next state
#   is done
# }

Experience = namedtuple("Experience",
                        ("state", "action", "reward", "next_state", "done"))

# ______________ ReplayMemory class  ______________ 
class ReplayMemory(object):

    """
        Class Determain how to save the data. \n
        Data will be save in ndarray with fix size. \n
        When the array is fill we will replace the oldes data \n
        (FIFO)
    """

    ###############
    # PRIVATE API #
    ###############

    # class constructor
    def __init__(self, capacity: int):
        """
            create instance with position 0.
            Params:
            --------
            capacity: int
                memory array size
        """
        self.capacity = capacity
        self.memory = list()
        self.position = 0

    # push one datapoint to memory buffer
    def _push_one(self, state, action, reward, next_state=None, done=None):
        """

            Push one DataPoint into memory

            --------
            Params:
            --------
            state: np.array
                the state of the env
            action: np.array
                action we activated
            reward: float 
                the reward we got
            next_state:
                state we finish in
            done: bool
                do we finish
        """
        # push new element if not in capacity size
        if len(self.memory) < self.capacity:
            self.memory.append(None)
        # insert into memory
        self.memory[self.position] = Experience(state, action, reward, next_state, done)
        self.position = (self.position + 1) % self.capacity


    ##############
    # PUBLIC API #
    ##############

    # push more then one element to memory
    def push(self, states, actions, rewards, next_states=None, dones=None):
        """
            push list of data point into memory
            --------
            @Params:
            --------
            state: np.array
                the state of the env
            action: np.array
                action we activated
            reward: float 
                the reward we got
            next_state:
                state we finish in
            done: bool
                do we finish
        """
        if isinstance(states, list):
            if next_states is not None and len(next_states) > 0:
                for s, a, r, n_s, d in zip(states, actions, rewards, next_states, dones):
                    self._push_one(s, a, r, n_s, d)
            else:
                for s, a, r in zip(states, actions, rewards):
                    self._push_one(s, a, r)
        else:
            self._push_one(states, actions, rewards, next_states, dones)

    # sample batch from memory randomly
    def sample(self, batch_size: int):
        """
            Randomly pick batch from memory

            --------
            Params:
            --------
            - Batch_size: int
                the number of data in single batch
        """
        if batch_size > len(self.memory):
            batch_size = len(self.memory)
        transitions = random.sample(self.memory, batch_size)
        return transitions

    # length of meomory 
    def __len__(self):
        return len(self.memory)
