import numpy as np

'''
    Defentions of state and what we take 
    from engine state
'''
class State:

    def __init__(self, engine):
        # get all vehicle in network
        vehicle_n:int = engine.get_vehicle_count()
        # avg travel time in the network
        vehicle_avg_travel_time:float = engine.get_average_travel_time()
        # map (lane)->(number of vehicle in lane)
        num_vehicle_in_each_lane:dict = engine.get_lane_vehicle_count()
        # map (lane)->(number of waiting vehicle in lane)
        num_waiting_vehicle_each_lane:dict = engine.get_lane_waiting_vehicle_count()
        # map (lane)->(list of vehicle in lane)
        vehicle_in_each_lane:dict = engine.get_lane_vehicles()
        # define the state var
        self.state = np.array([vehicle_avg_travel_time])

    def get_state(self):
        return self.state
