from API import Cityflow_API
from json_handler import JsonHandler

Cityflow_API






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



# = > get info from rl
# = > see new state in 


# = > get state in run time  || 
# = > 






