import os
from dotenv import load_dotenv

from src.models.DRL.mediator.API import Cityflow_API

f = open('states.txt', 'w')

f.write('start\n')

load_dotenv()
# crate city flow instance
api = Cityflow_API(os.getenv("CONFIG_JSON_FILE"))

# run the simulation and contralling eatch state
for i in range(100):
    # print(api.get_state())
    f.write(api.get_state().__str__()+'\n')

    if i == 50:
        api.set_action('intersection_1_1', 1)
    if i == 99:
        print(api.get_state())

    api.next_frame()

f.close()
