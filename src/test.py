import cityflow
import os
from dotenv import load_dotenv
from auto_option_builder import OptionBuilder
from json_handler import JsonHandler

load_dotenv()

eng = cityflow.Engine(os.getenv("CONFIG_JSON_FILE"))
lst = 5 #number of lightphases in roadnet file
j=0
for i in range(5000):
    if j >= lst:
        j = 0
    if i % 50:
        eng.set_tl_phase("intersection_1_1", j)
        j+=1
    eng.next_step()
print('Hello World')





# print(OptionBuilder.generate(30,4))

#JsonHandler.append_to_intersection("./simulation/json/roadnet", "intersection_0_0", [(2, [0, 1])])
# print(JsonHandler.read('./simulation/json/roadnet'))


#for i in range(1000):
    # if i == 500:
    # eng.set_tl_phase("intersection_0_0", 1)
    #eng.next_step()
# print(eng.get_current_time())


