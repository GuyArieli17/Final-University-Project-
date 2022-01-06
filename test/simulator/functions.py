import numpy as np

LANE_LENGTH  = 300
CAR_LENGTH = 5
NUMBER_OF_LANES = 12
CAR_INFO = 2
STATE_SIZE = ((LANE_LENGTH/CAR_LENGTH) * NUMBER_OF_LANES) * CAR_INFO

class RewardFunctions:

    
    @classmethod
    # reward by number of waiting cars
    def car_waiting(cls,prev_state: np.array, current_state: np.array) -> float:
        return float(np.sum(prev_state-current_state))
    @classmethod
    # reward by number of waiting cars
    def car_speed(cls,prev_state: np.array, current_state: np.array) -> float:
        return 0
    
# [
#   [name,,] 
# ]

class StateFunctions:
    
    @classmethod
    # state by number of waiting cars
    def car_waiting(cls,state: dict) -> np.array:
        lane_waiting_car_count = state['lane_waiting_vehicle_count']
        x = np.array([list(lane_waiting_car_count.values())], dtype=np.float64)
        return x

    @classmethod
    def car_speed(cls,state: dict) -> np.array:
        lane_vehicles_func = state['vehicle_info_func']
        vehicle_ids = np.array(state['vehicles'])
        st = state['lane_vehicles']
        print(st)
        # for v_id in vehicle_ids:
        #     print("ID:",v_id)
        #     road_info = lane_vehicles_func(v_id)
        #     return float(road_info['speed']),float(road_info['distance'])
        #     break
        return lane_vehicles_func(vehicle_ids[0])

