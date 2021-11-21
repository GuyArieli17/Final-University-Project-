import torch as th

import numpy as np

from models.Abstract.ReplayMemory import ReplayMemory
from models.Abstract.Utils import identity

class Agent:
    """
    """
    def __init__(self,env,state_dim:int,action_dim:int,
      memory_capacity=10000, max_steps=10000,
                 reward_gamma=0.99, reward_scale=1., done_penalty=None,
                 actor_hidden_size=32, critic_hidden_size=32,
                 actor_output_act=identity, critic_loss="mse",
                 actor_lr=0.01, critic_lr=0.01,
                 optimizer_type="rmsprop", entropy_reg=0.01,
                 max_grad_norm=0.5, batch_size=100, episodes_before_train=100,
                 epsilon_start=0.9, epsilon_end=0.01, epsilon_decay=200,
                 use_cuda=True)->None:
        