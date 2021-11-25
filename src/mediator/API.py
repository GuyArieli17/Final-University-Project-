import random
import cityflow
import numpy as np
from mediator.state import State
from mediator.actions import Action


class Cityflow_API:

    def __init__(self, config, dimension=[1, 1], n_steps=100):
        self.eng = cityflow.Engine(config)  # city flow engine
        self.n_steps = n_steps
        self.dimension = np.array(dimension)  # set the diminstion we will use
        self.number_of_state_delta = 0

    def next_frame(self):
        self.eng.next_step()

    def get_state(self) -> State:
        # Initiate a state instance
        state = State(self.eng)
        return state.get_state()

    def stochastic(self):
        # TODO: implemnt random routs from randoms cars
        rand_num = random.random()
        all_vehicles = self.eng.get_vehicles(include_waiting=False)
        waiting_vehicle_lst = self.eng.get_vehicles(include_waiting=True)
        driving_vehicle_lst = list(all_vehicles-waiting_vehicle_lst)

        for vehicle_id in driving_vehicle_lst:
            route = 0  # a list of road ids (doesn’t include the current road)
            speed = 0
            self.eng.set_vehicle_route(vehicle_id, route)  # retun T/F
            self.eng.set_vehicle_speed(vehicle_id, speed)

    def set_action(self, intersection_id: str, phase_id: int) -> bool:
        """
        phase_id - number of action which should to execute
        """
        # TODO: How to create a automaton network without changing the json
        # intersection_id = 0
        # phase_id
        self.eng.set_tl_phase(intersection_id, phase_id)
