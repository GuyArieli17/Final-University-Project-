import json
from ricxappframe.xapp_frame import RMRXapp, rmr
import numpy as np
from gym import spaces
from torch import nn
from torch import optim
from drl import DQN,ActorNetwork
#  ----------------- Const Params -----------------
_RESET_REQUEST = 60_000
_STEP_REQUEST = 61_000

_STATE_ACK = 60_001
_DONE_ACK = 61_001




#  ----------------- Xapp -----------------
class DRLXapp:

    """
        The Class is abstraction of RMRxapp.
        Will implment the function we will be needing
    """
    def __init__(self, fake_sdl=True) -> None:
        self._fake_sdl = fake_sdl
        self._xapp = RMRXapp(default_handler=self._default_handler,
                                post_init=self._post_init, use_fake_sdl= self._fake_sdl)
        ### bind funcation to message type
        # self._xapp.register_callback(self.send_reset, _RESET_REQUEST)
        # self._xapp.register_callback(self.send_reset, _STEP_REQUEST)
        

    def send_step(self):
        #Todo: implement
        self._xapp.rmr_send(json.dumps({"ping": number}).encode(), 6660666)
        pass

    def send_reset(self):
        #Todo: implement
        self._xapp.rmr_send(json.dumps({"ping": number}).encode(), 6660666)



    @staticmethod
    def default_handler(xapp,summary, sbuf):
        """
            Todo: add examles
        """
        xapp.logger.info("pong default handler called!")
        print("pong default handler received: {0}".format(summary))
        xapp.rmr_free(sbuf)



    @staticmethod
    def post_init(_xapp):
        """post init"""
        print("pong xapp could do some useful stuff here!")




    

    def run(self):
        self._xapp.run()


class MockEnvironment:
    
    def __init__(self, drl_xapp: DRLXapp) -> None:
        drl_xapp.

    def step(action: int):
        DRLXapp.
        pass

    def reset():
        pass



if __name__ == "__main__":
    drl_xapp = DRLXapp()
    drl_xapp.run()