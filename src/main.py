from mediator.API import Cityflow_API
from dotenv import load_dotenv
import os



load_dotenv()
# crate city flow instance
api = Cityflow_API(os.getenv("CONFIG_JSON_FILE"))
# run the simulation and contralling eatch state
for i in range(100):
    if i == 50:
        api.set_action(('intersection_1_1',1))
    if i == 99:
        print(api.get_state())
    api.next_frame()
    

