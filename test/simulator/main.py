from gym import spaces
import numpy as np
from simulation import Environment
from functions import StateFunctions,RewardFunctions
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

# Todo: add read me file with ecample + test file
if __name__ == "__main__":
    env = Environment(
        StateFunctions.car_speed,
        RewardFunctions.car_speed,
        ACTION_SPACE,
        OBSERVATION_SPACE,
        REWARD_RANGE,
        PATH,
    )
    for x in range(1_500):
        next_state, reward, done, _ = env.step(0)
        print(f"____________________________ Step: {x}")
        print("State:")
        print(f" \t {next_state}")
        print("Reward:")
        print(f" \t {reward}")
        print("Done:")
        print(f" \t {done}")
        break
