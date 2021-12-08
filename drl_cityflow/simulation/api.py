import random
import cityflow
import numpy as np


# from mediator.state import State
# from mediator.actions import Action

VEHICLE_LENGTH = 5.0
ROAD_LENGTH = 300.0
VEHICLE_MIN_GAP = 2.5

# class Helper:
#     # road_id = lane_key[:-2]
#     # if road_id not in road_id_dict:
#     #     road_id_dict[road_id] = []
#
#     @classmethod
#     def _convert_from_lane_dict_to_lane_dict_set(cls, lane_dict: dict) -> dict:
#         road_id_dict: dict = dict()
#         for lane_key, car_lst in lane_dict.items():
#             road_id_dict[lane_key] = set(car_lst)
#         return road_id_dict
#
#     @classmethod
#     def get_dict_of_running_cars_by_lane(cls, lane_all_cars: dict, lane_waiting_car: dict) -> dict:
#         if len(lane_waiting_car) != len(lane_all_cars):
#             IndexError("Length of lane_waiting_car_set is not equal to Length of lane_all_cars_set")
#         # body
#         lane_all_cars_set: dict = cls._convert_from_lane_dict_to_lane_dict_set(lane_all_cars)
#         lane_waiting_car_set: dict = cls._convert_from_lane_dict_to_lane_dict_set(lane_waiting_car)
#         rtn_dict: dict = dict()
#         # add card id of driving vehicle to rtn_dict
#         for lane_key in lane_all_cars_set.keys():
#             rtn_dict[lane_key] = lane_all_cars_set[lane_key] - lane_waiting_car_set[lane_key]
#         return rtn_dict
#
#     @classmethod
#     def get_lane_waiting_distance_by_lane(cls, lane_waiting_car_count: dict) -> dict:
#         rtn_dict: dict = dict()
#         for lane_id, vehicle_count in lane_waiting_car_count.items():
#             lane_capture: float = VEHICLE_MIN_GAP + vehicle_count * (VEHICLE_LENGTH + VEHICLE_MIN_GAP)
#             rtn_dict[lane_id] = ROAD_LENGTH - lane_capture
#         return rtn_dict
#
#     @classmethod
#     def get_dict_of_distance_by_car(cls, running_cars: dict) -> dict:
#
#         pass


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

    def state(self) -> np.array:
        vehicle_num: int = self.eng.get_vehicle_count()
        # avg travel time in the network
        vehicle_avg_travel_time: float = self.eng.get_average_travel_time()
        # map (lane)->(number of vehicle in lane)
        num_vehicle_in_each_lane: dict = self.eng.get_lane_vehicle_count()
        # map (lane)->(number of waiting vehicle in lane)
        lane_waiting_car_count: dict = self.eng.get_lane_waiting_vehicle_count()
        # map (lane)->(list of vehicle in lane)
        vehicle_in_each_lane: dict = self.eng.get_lane_vehicles()
        # map (lane)->(list of vehicle in lane)
        vehicle_waiting_in_each_lane: dict = self.eng.get_lane_waiting_vehicle_count()
        # get all running vehicle in each road
        # driving_cars_by_lane: dict = Helper.get_dict_of_running_cars_by_lane(
        #                                             vehicle_in_each_lane, vehicle_waiting_in_each_lane)
        # distance_to_each_lane: dict = Helper.get_lane_waiting_distance_by_lane(lane_waiting_car_count)
        return np.array([sum(list(lane_waiting_car_count.values()))])

    def reset(self) -> None:
        self.eng.reset()

    def next_frame(self) -> None:
        self.eng.next_step()

    def get_state(self) -> np.array:
        return self.state()

    def stochastic(self):
        # TODO: implemnt random routes from randoms cars
        rand_num = random.random()
        all_vehicles = self.eng.get_vehicles(include_waiting=False)
        waiting_vehicle_lst = self.eng.get_vehicles(include_waiting=True)
        driving_vehicle_lst = list(all_vehicles - waiting_vehicle_lst)

        for vehicle_id in driving_vehicle_lst:
            route = 0  # a list of road id's (doesn’t include the current road)
            speed = 0
            self.eng.set_vehicle_route(vehicle_id, route)  # retun T/F
            self.eng.set_vehicle_speed(vehicle_id, speed)

    def set_action(self, intersection_id: str, phase_id: int) -> None:
        """
        phase_id - number of action which should to execute
        """
        # TODO: How to create a automaton network without changing the json
        self.eng.set_tl_phase(intersection_id, phase_id)
