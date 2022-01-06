import numpy.random as rnd
import random
import json


# ____ import END ____
class Distribution:
    """
        this class implement all way's we 
        enter cars into the simuulation
    """
    @staticmethod
    # randonly add cars to the env
    def random(max_steps: int) -> list:
        """
            Randomly add cars to in.
        """
        return random.sample(range(max_steps),  random.randint(0, max_steps))

class FlowGenerator:

    """
        Generate json file (flow)
        that decide how the cars will enter the simulation.
        How to write Json file: https://cityflow.readthedocs.io/en/latest/flow.html
    """

    @staticmethod
    # create the Flow file 
    def compute(origin_file_path: str, new_file_path: str,
               max_steps: int, distribution_function: callable) -> json:
        """
            compute the flow file.

            @Params:
            ---------
            origin_file_path: str
                the path from we edit and extend
            new_file_path:  str
                where to save the flow file
            max_steps: int
                the maximum number of steps in the simulation
            distribution_function: callable
                how the car insertaion distribute 
        """
        # create data capture
        list_of_abstract_flow: list = []
        flow_lst: list = []
        # load orginal json
        with open(origin_file_path, "r") as flow_file:
            list_of_abstract_flow = json.load(flow_file)
        # run on original flow file and work with it
        for abstract_flow in list_of_abstract_flow:
            dist_list: list = distribution_function(max_steps)
            dist_list.sort()
            for timestamp in dist_list:
                dict_cpy = dict(abstract_flow)
                dict_cpy['startTime'] = timestamp
                dict_cpy['endTime'] = timestamp
                dict_cpy['interval'] = 1
                flow_lst.append(dict_cpy)
        json_file = json.dumps(flow_lst)
        with open(new_file_path, 'w') as new_flow:
            new_flow.write(json_file)
        return json_file