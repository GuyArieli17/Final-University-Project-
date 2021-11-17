import numpy as np
import cityflow


class Cityflow_API:

    def __init__(self,config,dimension=[1,1],n_steps=100) -> None:
        self.eng = cityflow.Engine(config) # city flow engine
        self.n_steps = n_steps
        self.dimension = np.array(dimension) # set the diminstion we will use

    def start(self):
        for i in range(100):
            if i == 99:
                print(self.get_state())
            self.next_frame()

    def next_frame(self)->None:
        self.eng.next_step()

    def get_state(self)-> dict:
        state = dict()
        n_vehicle = self.eng.get_vehicle_count()
        vehicle_lst = self.eng.get_vehicles(include_waiting=False)
        dict_by_lane = self.eng.get_lane_vehicle_count()
        dict_by_waiting = self.eng.get_lane_waiting_vehicle_count()
        state["n_vehicle"] = n_vehicle
        state["vehicle"] = vehicle_lst
        state["dict_by_lane"] = dict_by_lane
        state["dict_by_waiting"] = dict_by_waiting
        # get_lane_waiting_vehicle_count()
        # get_lane_vehicles()
        # get_vehicle_info(vehicle_id)
        # get_vehicle_speed()
        # get_vehicle_distance()
        # get_leader(vehicle_id)
        # get_current_time()
#         # get_average_travel_time()
        return state
#         

#     def set_action(self,action:np.array)->None:
#         pass

#     def next_frame(self)->None:
#         self.eng.next_step()
