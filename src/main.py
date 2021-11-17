from public.API import Cityflow_API
from dotenv import load_dotenv
import os



load_dotenv()
config = os.getenv("CONFIG_JSON_FILE")
api = Cityflow_API(config)
for i in range(100):
    if i == 50:
        api.set_action(('intersection_1_1',1))
    if i == 99:
        print(api.get_state())
    api.next_frame()
