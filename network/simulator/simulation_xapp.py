import json
from ricxappframe.xapp_frame import RMRXapp, rmr
import numpy as np
from gym import spaces
from simulation import Environment
# from ..const import *
#


#  ----------------- Const Params -----------------
START_ACTION = 62_000
GET_ACTION = 60_000

#  ----------------- Simulation Params -----------------
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
    x = np.array([list(lane_waiting_car_count.values())], dtype=np.float64)
    return x

class SimulationXapp:
    """
        Todo: add commends
    """

    def _set_action(self,xapp, summary, sbuf):
        # gather message
        message = json.loads(summary[rmr.RMR_MS_PAYLOAD])
        action = message['Action']
        print(f"[GOT] Action: {action}")
        # q_val = self._model(state)
        next_state, reward, done ,_  = self._env.step(action)
        # complie to json foramt
        next_state = next_state.tolist()
        print(f"[SEND]: next_state  reward done")
        xapp.rmr_rts(sbuf, new_payload=json.dumps({"State": [next_state,reward,done]}).encode(), new_mtype=GET_ACTION, retries=100)
        xapp.rmr_free(sbuf)
        

    def _default_handler(self,xapp, summary, sbuf):
        xapp.logger.info("pong default handler called!")
        xapp.rmr_free(sbuf)

    def _post_init(self,xapp):
        """post init"""
        print("__________________________")
        print("INIT SIMULATION XAPP !!!")
        print("__________________________")
        # state = self._env.reset()
        # print(f"Send: {state} to {6660666}")
        # message = json.dumps({"State": 0}).encode()
        # print(f"\t Message Sent: {message}")
        # xapp.rmr_send(message, 6660666)

    def _start(self,xapp, summary, sbuf):
        print("[START] connection....")
        xapp.rmr_free(sbuf)

    def __init__(self, trained_model_weight_path="./model_params.pth", fake_sdl=True) -> None:
        """
            Todo: dsadsada
        """
        #
        self._env = Environment(
            state_of_waiting_cars,
            reward_of_waiting_cars,
            ACTION_SPACE,
            OBSERVATION_SPACE,
            REWARD_RANGE,
            PATH,
        )
        self._fake_sdl = fake_sdl
        # Create Xapp instace
        self._xapp = RMRXapp(default_handler=self._default_handler, post_init=self._post_init, use_fake_sdl= self._fake_sdl)
        # Register Callback Functions
        self._xapp.register_callback(self._set_action, GET_ACTION)
        self._xapp.register_callback(self._start, START_ACTION)
        
    def run(self):
        self._xapp.run()



if __name__ == "__main__":
    drl_xapp = SimulationXapp()
    drl_xapp.run()































# # TEST 
# RANDOM_SEED = 2017
# ACTION_DIM = 8
# STATE_DIM = 24
# ACTION_SPACE = spaces.Box(
#     low=np.array([0]),  # Lower bound
#     high=np.array([8]),  # Upper bound
#     dtype=np.int64)
# REWARD_RANGE = (-np.inf, np.inf)
# OBSERVATION_SPACE = spaces.Box(
#     low=np.array([-np.inf for _ in range(STATE_DIM)]),  # Lower bound
#     high=np.array([np.inf for _ in range(STATE_DIM)]),  # Upper bound
#     dtype=np.int64)
# PATH = './config/config.json'
# def reward_of_waiting_cars(prev_state: np.array, current_state: np.array) -> float:
#     x = float(np.sum(prev_state-current_state))
#     return x

# def state_of_waiting_cars(state: dict) -> np.array:
#     lane_waiting_car_count: dict = state['lane_waiting_vehicle_count']
#     x = np.array([list(lane_waiting_car_count.values())], dtype=np.float)
#     return x

# def entry(self):
#     my_ns = "myxapp"

#     env = Environment(
#         state_of_waiting_cars,
#         reward_of_waiting_cars,
#         ACTION_SPACE,
#         OBSERVATION_SPACE,
#         REWARD_RANGE,
#         PATH,
#     )

#     number = 0
#     while True:
#         env.step(0)
#         # test healthcheck
#         print("ping is healthy? {}".format(xapp.healthcheck()))

#         # rmr send to default handler
#         self.rmr_send(json.dumps({"ping": number}).encode(), 6660666)

#         # rmr send 60000, should trigger registered callback
#         val = json.dumps({"test_send": number}).encode()
#         self.rmr_send(val, 60000)
#         number += 1

#         # store it in SDL and read it back; delete and read
#         self.sdl_set(my_ns, "ping", number)
#         self.logger.info(self.sdl_get(my_ns, "ping"))
#         self.logger.info(self.sdl_find_and_get(my_ns, "pin"))
#         self.sdl_delete(my_ns, "ping")
#         self.logger.info(self.sdl_get(my_ns, "ping"))

#         # rmr receive
#         for (summary, sbuf) in self.rmr_get_messages():
#             # summary is a dict that contains bytes so we can't use json.dumps on it
#             # so we have no good way to turn this into a string to use the logger unfortunately
#             # print is more "verbose" than the ric logger
#             # if you try to log this you will get: TypeError: Object of type bytes is not JSON serializable
#             print("ping: {0}".format(summary))
#             self.rmr_free(sbuf)

#         time.sleep(2)


# xapp = Xapp(entrypoint=entry, rmr_port=4564, use_fake_sdl=True)
# xapp.run()
