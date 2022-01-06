import json
from ricxappframe.xapp_frame import Xapp, rmr
import numpy as np
from torch import nn
from torch import optim
from drl import ActorNetwork
import torch as th
import time

#  ----------------- Const Params -----------------
START_ACTION = 62_000
GET_ACTION = 60_000
ACTION_TYPE = 61_000

#  ----------------- Model Params -----------------

ACTION_DIM = 8
STATE_DIM = 24
HIDDEN_LAYER = 50


class DRLXapp:
    """
        Todo: add commends
    """
    def _loop(self, xapp):
        # TODO: change the action using action = drawSimilarAction(action)
        # TODO: change the state using state = adjustState(state)
        print("\t Start loop: ")
        start_connection = json.dumps({"test_send": 0}).encode()
        print(f"[SEND] start: {start_connection}")
        xapp.rmr_send(start_connection, START_ACTION)
        action = 8
        while True:
            action_json = json.dumps({"Action": action}).encode()
            xapp.rmr_send(action_json, GET_ACTION)
            for (summary, sbuf) in xapp.rmr_get_messages():
                message = json.loads(summary[rmr.RMR_MS_PAYLOAD])
                print("[GOT]: {0}".format(message))
                next_state, reward, done = message['State']
                action = int(th.argmax(self._model(th.tensor(next_state).float())))
                xapp.rmr_free(sbuf)
            time.sleep(0.01)

    def __init__(self, trained_model_weight_path="./model_params.pth", fake_sdl=True) -> None:
        """
            Todo: dsadsada
        """
        # Load Model From Memory
        self._model = ActorNetwork(STATE_DIM, HIDDEN_LAYER, ACTION_DIM, nn.ReLU())
        self._model.load_state_dict(th.load(trained_model_weight_path))
        self._fake_sdl = fake_sdl
        # Create Xapp instace
        self._xapp = Xapp(entrypoint=self._loop, rmr_port=4564, use_fake_sdl=True)
        # Register Callback Functions

    def run(self):
        self._xapp.run()


if __name__ == "__main__":
    drl_xapp = DRLXapp()
    drl_xapp.run()