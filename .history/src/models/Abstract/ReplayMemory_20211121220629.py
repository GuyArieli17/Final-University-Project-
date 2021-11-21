import numpy as np
from models.Abstract.Experience import Experience

"""
    Object That Mannage All Access To The Buffer
    We User Buffer To Remove Corlation Between Samples
"""
class ReplayMemory(object):
    def __init__(self, capacity: int) -> None:
        self.capacity = capacity # the length of the buffer
        self.memory = np.array([None for i in range(self.capacity)], dtype=Experience) # create the buffer
        self.current_indx = 0 # the index to insert next sample
        self.length = 0

    def _push_one(self, state, action, reward, next_state=None, done=None)->None:
        """  add to the end of the buffer (if full replace with the least recent added)  """
        self.memory[self.current_indx] = Experience(state, action, reward, next_state, done)
        self.current_indx = (self.current_indx + 1) % self.capacity
        self.length += (self.length < self.capacity)

    def push(self, states, actions, rewards, next_states, dones):
        """ eatch argument is np.array in the same length """
        for state, action, reward, next_state, done in zip(states, actions, rewards, next_states, dones):
            self._push_one(state, action, reward, next_state, done)

    def sample(self, batch_size):
        """  sample batch_size sample from memeory in random form   """
        batch_size = min(self.capacity, batch_size)  # overhead of cpacity
        pick_indexes = np.random.choice(self.capacity, batch_size, replace=False)
        batch = self.memory[pick_indexes]
        return batch

    def __len__(self):
        return self.length
