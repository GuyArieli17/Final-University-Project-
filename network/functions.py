import numpy as np

class RewardFunctions:

    
    @classmethod
    # reward by number of waiting cars
    def car_waiting(cls,prev_state: np.array, current_state: np.array) -> float:
        return float(np.sum(prev_state-current_state))

    





class StateFunctions:
    
    @classmethod
    # state by number of waiting cars
    def car_waiting(cls,state: dict) -> np.array:
        lane_waiting_car_count: dict = state['lane_waiting_vehicle_count']
        x = np.array([list(lane_waiting_car_count.values())], dtype=np.float64)
        return x

    @classmethod
    def car_speed

