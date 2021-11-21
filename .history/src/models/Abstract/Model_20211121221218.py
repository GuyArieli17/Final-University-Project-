import torch as th
from torch import nn

class AgetNetwork(nn.Module):
    def __init__(self, state_dim, hidden_size, output_size, output_act) -> None:
        super(AgetNetwork,self).__init__()
        self.fc1 = nn.Linear(state_dim,hidden_size)
        self.fc2 = nn.Linear(hidden_size,hidden_size)
        self.fc3 = nn.Linear(hidden_size,output_size)
        self.output_act = output_act

    def __call__(self, input):
        out = nn.functional.relu(self.fc1(input))
        out = nn.functional.relu(self.fc2(out))
        out = self.output_act(self.fc3(out))
        return out