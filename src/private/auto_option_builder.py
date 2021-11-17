import cityflow
import os
from dotenv import load_dotenv

class OptionBuilder:
    @staticmethod 
    def generate(num_secound,lane_range):
        options = [] # [ (10,[1,2])] 
        for sec in range(num_secound):
            for lane_1 in range(lane_range):
                for lane_2 in range(lane_1+1,lane_range):
                    options.append((sec,[lane_1,lane_2]))
        return options
                
                
        



#TODO: open roadnet file 
#TODO: genrate all options