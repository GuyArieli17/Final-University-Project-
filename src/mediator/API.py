import numpy as np
import cityflow
import random

class Cityflow_API:

    def __init__(self,config,dimension=[1,1],n_steps=100) -> None:
        self.eng = cityflow.Engine(config) # city flow engine
        self.n_steps = n_steps
        self.dimension = np.array(dimension) # set the diminstion we will use
        self.number_of_state_delta = 0

    def next_frame(self)->None:
        self.eng.next_step()

    def get_state(self)-> dict:
        state = dict()
        n_vehicle = self.eng.get_vehicle_count()
        vehicle_lst = self.eng.get_vehicles(include_waiting=False)
        dict_by_lane = self.eng.get_lane_vehicle_count()
        dict_by_waiting = self.eng.get_lane_waiting_vehicle_count()
        avg_travel_time = self.eng.get_average_travel_time()
        # state["n_vehicle"] = n_vehicle
        # state["vehicle"] = vehicle_lst
        # state["dict_by_lane"] = dict_by_lane
        # state["dict_by_waiting"] = dict_by_waiting
        state["avg_travel_time"] = avg_travel_time
        # get_lane_vehicles()
        # get_vehicle_info(vehicle_id)
        # get_vehicle_speed()
        # get_vehicle_distance()
        # get_leader(vehicle_id)
        # get_current_time()
        return state

    def stochastic(self):
        #TODO: implemnt random routs from randoms cars
        rnd_num = random.random()
        vehicle_id = None
        route = None
        speed = 0
        self.eng.set_vehicle_route(vehicle_id,route)
        self.eng.set_vehicle_speed(vehicle_id, speed)

    def set_action(self,action:list)->None:
        #TODO: How to autamte network without changing the json
        intersection_id , phase_id = action
        self.eng.set_tl_phase(intersection_id, phase_id)
