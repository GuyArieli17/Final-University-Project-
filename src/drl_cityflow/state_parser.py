import numpy as np


def sum_of_waiting_cars(state: dict) -> np.array:
    lane_waiting_car_count: dict = state['lane_waiting_vehicle_count']
    return np.array([sum(list(lane_waiting_car_count.values()))], dtype=np.float)


def state_of_waiting_cars(state: dict) -> np.array:
    lane_waiting_car_count: dict = state['lane_waiting_vehicle_count']
    x = np.array([list(lane_waiting_car_count.values())], dtype=np.float)
    return x
