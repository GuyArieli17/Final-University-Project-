from drl import ActorNetwork, DQN
# if not install in current lib write : 
#      - cd ../../library/simulator-moudle
#      - pip install .
from torch import nn


# TEST 
ACTION_DIM = 8
STATE_DIM = 24
HIDDEN_LAYER = 50

actor_network = ActorNetwork(STATE_DIM,HIDDEN_LAYER, ACTION_DIM, nn.ReLU())
# model = DQN()
# Todo: add read me file with ecample + test file
if __name__ == "__main__":
    print("FINISH TEST")