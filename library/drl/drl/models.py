# ==================================================================================
#       Copyright (c) 2019-2022 Guy Arieli (GuyArieli17)
#       Copyright (c) 2018-2020 Eran
#       Copyright (c) 2018-2020 Amit
#
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
# ==================================================================================
import torch as th
from torch import nn
import numpy as np

# ______________ ActorNetwork class  ______________ 
class ActorNetwork(nn.Module):

    """
        Simple 3 Fully connected articture
        with relu after each one
        with user activation function
        ----------------------------
        Extends [nn.Module]
    """

    def __init__(self, state_dim, hidden_size, output_size, output_act):
        """
            Params:
            ---------
            - state_dim [int]:   input size as state
            - hidden_size [int]:   hidden layer size x2
            - output_size [int]:   size of model output (last layer)
            - output_act[nn.Function]: activation function on last layer
        """
        super(ActorNetwork, self).__init__()
        self.fc1 = nn.Linear(state_dim, hidden_size)
        self.fc2 = nn.Linear(hidden_size, hidden_size)
        self.fc3 = nn.Linear(hidden_size, output_size)
        self.output_act = output_act

    def forward(self, state):
        out = nn.functional.relu(self.fc1(state))
        out = nn.functional.relu(self.fc2(out))
        out = self.output_act(self.fc3(out))
        return out

class RecurrentNeuralNetwork(nn.Module):
    """
        Todo: implement
    """
    def __init__(self, state_dim, hidden_size, n_layers, output_size, output_act, batch_size):
        """
            Params:
            ---------
            - state_dim [int]:   input size as state
            - hidden_size [int]:   hidden layer size x2
            - output_size [int]:   size of model output (last layer)
            - output_act[nn.Function]: activation function on last layer
        """
        super(RecurrentNeuralNetwork, self).__init__()
        print(f'hidden_size: {hidden_size}')
        print(f'n_layers: {n_layers}')
        print(f'state_dim: {state_dim}')
        print(f'output_act: {output_act}')
        print(f'batch_size: {batch_size}')
        print(f'output_size: {output_size}')
        self.hidden_size = hidden_size
        self.n_layers = n_layers
        self.state_dim = state_dim
        self.output_act = output_act
        self.batch_size = batch_size
        self.output_size = output_size
        self.rnn = nn.RNN(input_size=self.state_dim, hidden_size=self.hidden_size, num_layers=self.n_layers,
                          batch_first=False)
        self.fc = nn.Linear(self.hidden_size, self.output_size)

    def forward(self, states):
        print(states.size())
        hidden = self.init_hidden()
        out, hidden = self.rnn(states, hidden)
        out = out.contiguous().view(-1, self.hidden_size)
        out = self.fc(out)
        out = self.output_act(out)
        return out

    def init_hidden(self):
        hidden = th.zeros(self.n_layers, 1, self.hidden_size)
        return hidden

class ConvNetwork(nn.Module):
    """
        Todo implement
    """
    def __init__(self, state_dim, hidden_size, n_layers, output_size, output_act):
        super(ConvNetwork, self).__init__()
        self.hidden_dim = hidden_size
        self.n_layers = n_layers
        self.rnn = nn.RNN(state_dim, hidden_size, n_layers, batch_first=True)
        self.fc = nn.Linear(hidden_size, output_size)

    def forward(self, state):
        batch_size = state.size(0)
        hidden = self.init_hidden(batch_size)
        out, hidden = self.rnn(state, hidden)
        out = out.contiguous().view(-1, self.hidden_dim)
        out = self.fc(out)
        out = self.output_act(out)
        return out, hidden

    def init_hidden(self, batch_size):
        hidden = th.zeros(self.n_layers, batch_size, self.hidden_dim)
        return hidden
