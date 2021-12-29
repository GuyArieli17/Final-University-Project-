from gym import spaces
import numpy as np
from simulation import TrafficSteeringEnvironment
# if not install in current lib write : 
#      - cd ../../library/simulator-moudle
#      - pip install .

# TEST 
RANDOM_SEED = 2017
ACTION_DIM = 8
STATE_DIM = 24

ACTION_SPACE = spaces.Box(
    low=np.array([0]),  # Lower bound
    high=np.array([8]),  # Upper bound
    dtype=np.int64)
REWARD_RANGE = (-np.inf, np.inf)
OBSERVATION_SPACE = spaces.Box(
    low=np.array([-np.inf for _ in range(STATE_DIM)]),  # Lower bound
    high=np.array([np.inf for _ in range(STATE_DIM)]),  # Upper bound
    dtype=np.int64)
PATH = './config/config.json'

def reward_of_waiting_cars(prev_state, current_state):
    x = float(np.sum(prev_state-current_state))
    return x

def state_of_waiting_cars(state):
    lane_waiting_car_count = state['lane_waiting_vehicle_count']
    x = np.array([list(lane_waiting_car_count.values())], dtype=np.float)
    return x

# Todo: add read me file with ecample + test file
if __name__ == "__main__":
    x = TrafficSteeringEnvironment(
        state_of_waiting_cars,
        reward_of_waiting_cars,
        ACTION_SPACE,
        OBSERVATION_SPACE,
        REWARD_RANGE,
        PATH,
    )
    print("FINISH TEST")