import numpy as np
from helper import ClusterMannager
LANE_LENGTH  = 300
CAR_LENGTH = 5
NUMBER_OF_LANES = 12
CAR_INFO = 2
STATE_SIZE = ((LANE_LENGTH/CAR_LENGTH) * NUMBER_OF_LANES) * CAR_INFO

road_mapper = {
    "road_0_1_0": 0,
    "road_1_0_1": 0,
    "road_2_1_2": 0,
    "road_1_2_3": 0,
    "road_1_1_0": 0,
    "road_1_1_1": 0,
    "road_1_1_2": 0,
    "road_1_1_3": 0,
}



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
        cm = ClusterMannager()
        vehicle_ids = np.array(state['vehicles'])
        print("___________________________")
        for car_id in vehicle_ids:
            id = car_id[:-2]
            print(id)
            # road_mapper
        #     cm.push_car_to_cluster_info
        # lane_vehicles_func = state['vehicle_info_func']
        
        # st = state['lane_vehicles']
        # print(st)
        # for v_id in vehicle_ids:
        #     print("ID:",v_id)
        #     road_info = lane_vehicles_func(v_id)
        #     return float(road_info['speed']),float(road_info['distance'])
        #     break
        return []

