# ---------------- IMPROTS ----------------
import random
import cityflow
import numpy as np

# ---------------- HYPER PARAMATERS ----------------
VEHICLE_LENGTH = 5.0
ROAD_LENGTH = 300.0
VEHICLE_MIN_GAP = 2.5

# ---------------- API ----------------
class CityFlowAPI:

    """
        API
    """

    def __init__(self, config: str, dimension=[1, 1], n_steps=100) -> None:
        # init and create city flow engine
        self.eng = cityflow.Engine(config)
        # number of max steps
        self.n_steps = n_steps
        self.dimension = np.array(dimension)  # set the dim we will use
        self.number_of_state_delta = 0

    def state(self) -> dict:
        rtn_state = dict()
        rtn_state['vehicle_count'] = self.eng.get_vehicle_count()
        # avg travel time in the network
        rtn_state['average_travel_time'] = self.eng.get_average_travel_time()
        # map (lane)->(number of vehicle in lane)
        rtn_state['lane_vehicle_count'] = self.eng.get_lane_vehicle_count()
        # map (lane)->(number of waiting vehicle in lane)
        rtn_state['lane_waiting_vehicle_count'] = self.eng.get_lane_waiting_vehicle_count()
        # map (lane)->(list of vehicle in lane)
        rtn_state['lane_vehicles'] = self.eng.get_lane_vehicles()
        return rtn_state

    def reset(self) -> None:
        self.eng.reset()

    def next_frame(self) -> None:
        self.eng.next_step()

    def get_state(self) -> np.array:
        return self.state()

    def stochastic(self):
        pass
        # TODO: implemnt random routes from randoms cars
        # rand_num = random.random()
        # all_vehicles = self.eng.get_vehicles(include_waiting=False)
        # waiting_vehicle_lst = self.eng.get_vehicles(include_waiting=True)
        # driving_vehicle_lst = list(all_vehicles - waiting_vehicle_lst)

        # for vehicle_id in driving_vehicle_lst:
        #     route = 0  # a list of road id's (doesn’t include the current road)
        #     speed = 0
        #     self.eng.set_vehicle_route(vehicle_id, route)  # retun T/F
        #     self.eng.set_vehicle_speed(vehicle_id, speed)

    def set_action(self, intersection_id: str, phase_id: int) -> None:
        """
            phase_id - number of action which should to execute
        """
        # TODO: How to create a automaton network without changing the json
        self.eng.set_tl_phase(intersection_id, phase_id)


if __name__ == "__main__":
    print("Hello world")