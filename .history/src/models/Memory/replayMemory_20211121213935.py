import numpy as np
from models.Memory.Experience import Experience
import random

class ReplayMemory(object):
    def __init__(self,capacity:int) -> None:
        self.capacity = capacity
        self.memory = np.array([None for i in range(self.capacity)],dtype=Experience)
        self.current_indx = 0

    def _push_one(self,state,action,reward,next_state=None,done=None):
        self.memory[self.current_indx] = Experience(state, action, reward, next_state, done)
        self.position = (self.position + 1) % self.capacity

    def push(self, states, actions, rewards, next_states, dones):
        for state,action,reward,next_state,done in zip(states, actions, rewards, next_states, dones):
            self._push_one(state,action,reward,next_state,done)

    def sample(self, batch_size):
        batch_size = min(self.capacity,batch_size) # overhead of cpacity
        transitions = random.sample(self.memory, batch_size) # pick random 
        batch = Experience(*zip(*transitions))
        return batch

    def __len__(self):
        return len(self.memory)