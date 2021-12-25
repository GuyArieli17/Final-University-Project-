import numpy as np


def reward_func_implementation_1(prev_state: np.array, current_state: np.array) -> float:
    return prev_state - current_state


def reward_of_waiting_cars(prev_state: np.array, current_state: np.array) -> float:
    x = float(np.sum(prev_state-current_state))
    return x
