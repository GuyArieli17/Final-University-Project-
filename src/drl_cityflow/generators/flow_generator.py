import numpy.random as rnd
import random
import json


# ____ import END ____
class Distribution:
    @staticmethod
    def random(max_steps) -> list[int]:
        return random.sample(range(max_steps),  random.randint(0, max_steps))


class FlowGenerator:
    """
        Do something
    """
    @staticmethod
    def create(origin_file_path: str, new_file_path: str,
               max_steps: int, distribution_function: callable) -> json:
        list_of_abstract_flow: list = []
        flow_lst: list = []
        # open file and save in var data
        with open(origin_file_path, "r") as flow_file:
            list_of_abstract_flow = json.load(flow_file)
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


# if __name__ == '__main__':
#     flow_lst = FlowGenerator.create('../simulation/config/abstract_flow.json', '../simulation/config/flow.json',
#                                                                                 250, Distribution.random)
