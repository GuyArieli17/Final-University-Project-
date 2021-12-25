import torch as th
from torch import nn
from pathlib import Path
import os, sys


currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)

# class ActorNetwork(nn.Module):
#     """
#     A network for actor
#     """
#     def __init__(self, state_dim, hidden_size, output_size, output_act):
#         super(ActorNetwork, self).__init__()
#         self.fc1 = nn.Linear(state_dim, hidden_size)
#         self.fc2 = nn.Linear(hidden_size, hidden_size)
#         self.fc3 = nn.Linear(hidden_size, output_size)
#         self.output_act = output_act

#     def forward(self, state):
#         out = nn.functional.relu(self.fc1(state))
#         out = nn.functional.relu(self.fc2(out))
#         out = self.output_act(self.fc3(out))
#         return out

from drl_cityflow.simple.models import ActorNetwork


ACTION_DIM = 8
STATE_DIM = 24
HIDDEN_LAYER = 50


def init__dqn_model():
    # model = ActorNetwork(STATE_DIM, HIDDEN_LAYER, ACTION_DIM, nn.ReLU())
    model_file_name = 'model.pth'
    model__file_path = Path(__file__).with_name(model_file_name)
    # model.load_state_dict(th.load(model__file_path))
    model = th.load(model__file_path)
    optimizer = th.optim.Adam(_model.parameters())
    
    return model, optimizer


_model, _optimizer = init__dqn_model()

# Print model's state_dict
print("Model's state_dict:")
for param_tensor in _model.state_dict():
    print(param_tensor, "\t", _model.state_dict()[param_tensor].size())

# Print optimizer's state_dict
print("Optimizer's state_dict:")
for var_name in _optimizer.state_dict():
    print(var_name, "\t", _optimizer.state_dict()[var_name])