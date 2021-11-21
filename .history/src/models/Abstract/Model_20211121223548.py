import torch as th
from torch import nn

class AgetNetwork(nn.Module):
    """
        Agent Network moudle
    """
    def __init__(self, state_dim:int, hidden_size:int, output_size:int, output_action:th.functional) -> None:
        """ Build the Network 3 fully connectted layers """
        super(AgetNetwork,self).__init__()
        self.fc1 = nn.Linear(state_dim,hidden_size)
        self.fc2 = nn.Linear(hidden_size,hidden_size)
        self.fc3 = nn.Linear(hidden_size,output_size)
        # set the output activation finction
        self.output_action = output_action

    def __call__(self, state:th.tensor)->th.tensor:
        """ connect each layer of network [do foward pass   ] """
        fc1_output = nn.functional.relu(self.fc1(state))
        fc2_output = nn.functional.relu(self.fc2(fc1_output))
        fc3_output = self.output_action(self.fc3(fc2_output))
        return fc3_output

class CriticNetwork(nn.Module):
    """
        A network for critic
    """
    def __init__(self, state_dim:int, action_dim:int, hidden_size:int, output_size=1):
        """ Build the Network 3 fully connectted layers """
        super(CriticNetwork, self).__init__()
        self.fc1 = nn.Linear(state_dim, hidden_size)
        self.fc2 = nn.Linear(hidden_size + action_dim, hidden_size)
        self.fc3 = nn.Linear(hidden_size, output_size)

    def __call__(self, state:th.tensor, action:th.tensor)->th.tensor:
        """ connect each layer of network [do foward pass ] """
        fc1_output = nn.functional.relu(self.fc1(state))
        fc2_output_insert_action = th.cat([fc1_output, action], 1) # n array vecor
        fc2_output = nn.functional.relu(self.fc2(fc2_output_insert_action))
        fc3_output = self.fc3(fc2_output)
        return fc3_output

class ActorCriticNetwork(nn.Module):
    """
    An actor-critic network that shared lower-layer representations but
    have distinct output layers
    """
    def __init__(self, state_dim:int, action_dim:int, hidden_size:int, actor_output_action:th.functional, critic_output_size=1):
        """ Combine both Actor & crtic and stack with 2 fc layers"""
        super(ActorCriticNetwork, self).__init__()
        self.fc1 = nn.Linear(state_dim, hidden_size)
        self.fc2 = nn.Linear(hidden_size, hidden_size)
        self.actor_linear = nn.Linear(hidden_size, action_dim)
        self.critic_linear = nn.Linear(hidden_size, critic_output_size)
        self.actor_output_act = actor_output_action

    def __call__(self, state:th.tensor)->th.tensor:
        """ connect each layer of network [do foward pass ] """
        out = nn.functional.relu(self.fc1(state))
        out = nn.functional.relu(self.fc2(out))
        act = self.actor_output_action(self.actor_linear(out))
        val = self.critic_linear(out)
        return act, val
