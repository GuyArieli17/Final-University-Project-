import numpy as np


class State:

    def __init__(self, engine):
        self.state_dict = dict()

        # count_vehicle : int
        # return the number of total running vehicles
        count_vehicle = engine.get_vehicle_count()

        # count_vehicle_by_lane : dict
        # return a dict with lane id as key and the vehicle number as value
        count_vehicle_by_lane = engine.get_lane_vehicle_count()

        # count_vehicle_waiting_by_lane : dict
        # return a dict with lane id as key and the number of waiting vehicles as value
        count_vehicle_waiting_by_lane = engine.get_lane_waiting_vehicle_count()

        # avg_travel_time : dict
        # return a dict with lane id as key and the number of waiting vehicles as value
        avg_travel_time = engine.get_average_travel_time()

        self.state = np.array([
            count_vehicle,
            count_vehicle_by_lane,
            count_vehicle_waiting_by_lane,
            avg_travel_time
        ])

        # vehicle_lst = self.eng.get_vehicles(include_waiting=False) # get vehicle ids
        # vehicle_lst = self.eng.get_vehicles(include_waiting=True) # get vehicle ids which waiting
        # get_lane_vehicles()
        # get_vehicle_info(vehicle_id)
        # get_vehicle_speed()
        # get_vehicle_distance()
        # get_leader(vehicle_id)
        # get_current_time()

    def get_state(self):
        return self.state_dict
