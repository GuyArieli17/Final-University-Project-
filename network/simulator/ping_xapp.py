import time
import json
from ricxappframe.xapp_frame import Xapp
from simulation import Environment
from gym import spaces
import numpy as np

# TEST 
RANDOM_SEED = 2017
ACTION_DIM = 8
STATE_DIM = 24
ACTION_SPACE = spaces.Box(
    low=np.array([0]),  # Lower bound
    high=np.array([8]),  # Upper bound
    dtype=np.int64)
REWARD_RANGE = (-np.inf, np.inf)
OBSERVATION_SPACE = spaces.Box(
    low=np.array([-np.inf for _ in range(STATE_DIM)]),  # Lower bound
    high=np.array([np.inf for _ in range(STATE_DIM)]),  # Upper bound
    dtype=np.int64)
PATH = './config/config.json'
def reward_of_waiting_cars(prev_state: np.array, current_state: np.array) -> float:
    x = float(np.sum(prev_state-current_state))
    return x

def state_of_waiting_cars(state: dict) -> np.array:
    lane_waiting_car_count: dict = state['lane_waiting_vehicle_count']
    x = np.array([list(lane_waiting_car_count.values())], dtype=np.float)
    return x

def entry(self):
    my_ns = "myxapp"

    env = Environment(
        state_of_waiting_cars,
        reward_of_waiting_cars,
        ACTION_SPACE,
        OBSERVATION_SPACE,
        REWARD_RANGE,
        PATH,
    )

    number = 0
    while True:
        env.step(0)
        # test healthcheck
        print("ping is healthy? {}".format(xapp.healthcheck()))

        # rmr send to default handler
        self.rmr_send(json.dumps({"ping": number}).encode(), 6660666)

        # rmr send 60000, should trigger registered callback
        val = json.dumps({"test_send": number}).encode()
        self.rmr_send(val, 60000)
        number += 1

        # store it in SDL and read it back; delete and read
        self.sdl_set(my_ns, "ping", number)
        self.logger.info(self.sdl_get(my_ns, "ping"))
        self.logger.info(self.sdl_find_and_get(my_ns, "pin"))
        self.sdl_delete(my_ns, "ping")
        self.logger.info(self.sdl_get(my_ns, "ping"))

        # rmr receive
        for (summary, sbuf) in self.rmr_get_messages():
            # summary is a dict that contains bytes so we can't use json.dumps on it
            # so we have no good way to turn this into a string to use the logger unfortunately
            # print is more "verbose" than the ric logger
            # if you try to log this you will get: TypeError: Object of type bytes is not JSON serializable
            print("ping: {0}".format(summary))
            self.rmr_free(sbuf)

        time.sleep(2)


xapp = Xapp(entrypoint=entry, rmr_port=4564, use_fake_sdl=True)
xapp.run()
