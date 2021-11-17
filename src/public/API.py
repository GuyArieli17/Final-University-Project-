import numpy as np
import cityflow
import os
from dotenv import load_dotenv
from auto_option_builder import OptionBuilder


class Cityflow_API:

    def __init__(self,dimension=[1,1]) -> None:
        self.eng = cityflow.Engine(os.getenv("CONFIG_JSON_FILE")) # city flow engine
        self.dimension = np.array(dimension) # set the diminstion we will use


    def get_state(self)-> np.array:
        get_vehicle_count();
        get_vehicles(include_waiting=False)
        get_lane_vehicle_count()
        get_lane_waiting_vehicle_count()
        get_lane_vehicles()
        get_vehicle_info(vehicle_id)
        get_vehicle_speed()
        get_vehicle_distance()
        get_leader(vehicle_id)
        get_current_time()
        get_average_travel_time()
        pass

    def set_action(self,action:np.array)->None:
        pass

    def next_frame(self)->None:
        self.eng.next_step()
