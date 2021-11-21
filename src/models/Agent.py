import torch as th
import numpy as np

class Agent:

    def __init__(self,env,state_dim,action_dim) -> None:
        self.env = env
        