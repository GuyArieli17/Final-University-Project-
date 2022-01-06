# ==================================================================================
#       Copyright (c) 2019-2022 Guy Arieli (GuyArieli17)
#       Copyright (c) 2018-2020 Eran
#       Copyright (c) 2018-2020 Amit
#
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
# ==================================================================================

import cityflow
import numpy as np


class CityFlowAPI:

    """
    This class is abstraction of CityFlowAPI: https://cityflow.readthedocs.io/en/latest/start.html#data-access-api
    It's easy to maintain and change withput a need to update the rest of the code
    """

    ###############
    # PRIVATE API #
    ###############

    # the length of vehicle on doc
    _VEHICLE_LENGTH = 5.0
    # the length of road in the config file
    _ROAD_LENGTH = 300.0
    # the gap determine in the config file
    _VEHICLE_MIN_GAP = 2.5

    # class constructor
    def __init__(self, config: str, dimension=[1, 1], steps=100) -> None:
        """
            @Parameters
            ----------
            configh: str
                A relative path to the config file
            dimension: np.array
                Array that determine the length of .. 
            steps: int
                Number of step the simulation will do before reset
            ----------
        """
        self._eng = cityflow.Engine(config)
        self._steps = steps
        self._dimension = np.array(dimension)
        self._state_delta = 0

    ##############
    # PUBLIC API #
    ##############
    
    # get the state of the simulation(Cityflow)
    def state(self) -> dict:
        """
            Get all data from simulation and reorganize 
            it, remove the unnecessary data and preforme some
            function to clean the data. 

            @Parameters
            ----------
            None
            ----------

            @Returns
            -----------
            State: 
                a dict with all necessary data
            ----------
        """
        rtn_state = dict()
        rtn_state['vehicle_count'] = self._eng.get_vehicle_count()
        # avg travel time in the network
        rtn_state['average_travel_time'] = self._eng.get_average_travel_time()
        # map (lane)->(number of vehicle in lane)
        rtn_state['lane_vehicle_count'] = self._eng.get_lane_vehicle_count()
        # map (lane)->(number of waiting vehicle in lane)
        rtn_state['lane_waiting_vehicle_count'] = self._eng.get_lane_waiting_vehicle_count()
        # map (lane)->(list of vehicle in lane)
        rtn_state['lane_vehicles'] = self._eng.get_lane_vehicles()
        #Todo: add
        rtn_state['vehicle_info_func'] = self._eng.get_vehicle_info
        #Todo: add
        rtn_state['vehicles'] = self._eng.get_vehicles(include_waiting=False)
        return rtn_state

    # reset the simulatio and all class data
    def reset(self) -> None:
        self._eng.reset()

    # call simulation next step
    def next_frame(self) -> None:
        self._eng.next_step()

    # TODO: the function will add stochatic to the simaltion
    def stochastic(self):
        # TODO: implemnt random routes from randoms cars
        pass

    # set the next step of the simulation
    def set_action(self, intersection_id: str, phase_id: int) -> None:
        """
            Get action (index of phase in intersection flow file - we wrote beffore running)
            and activate the function in the simulator(cityflow)
        
            @Parameters
            ----------
            intersection_id: str
                an id of the intersection we want to activate 
                the action on
            phase_id: str
                an index of the phase in the 
                jason file
            ----------
            @Returns
            -----------
            State: 
                None
            ----------
        """
        self._eng.set_tl_phase(intersection_id, phase_id)
