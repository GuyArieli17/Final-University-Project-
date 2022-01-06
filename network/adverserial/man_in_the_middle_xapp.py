import json

from ricxappframe.xapp_frame import rmr, RMRXapp

#  ----------------- Const Params -----------------
from network.adverserial.utils import drawSimilarAction, adjustState

START_ACTION = 62_000
GET_ACTION = 60_000
ADVERSARIAL_TYPE = 61_000

#  ----------------- Model Params -----------------

ACTION_DIM = 8
STATE_DIM = 24
HIDDEN_LAYER = 50


def post_init(_self):
    """post init"""
    print("pong xapp could do some useful stuff here!")


def sixtyh(self, summary, sbuf):
    message = json.loads(summary[rmr.RMR_MS_PAYLOAD])
    action = message['Action']
    action = drawSimilarAction(action)
    action_json = json.dumps({"Action": action}).encode()
    xapp.rmr_send(action_json, ADVERSARIAL_TYPE)

    summary = xapp.rmr_get_messages()
    message = json.loads(summary[rmr.RMR_MS_PAYLOAD])
    print("[GOT]: {0}".format(message))
    next_state, reward, done = message['State']
    next_state = adjustState(next_state)
    state_json = json.dumps({"State": [next_state, reward, done]}).encode()
    self.rmr_rts(sbuf, new_payload=state_json, new_mtype=GET_ACTION, retries=100)
    self.rmr_free(sbuf)


def defh(self, summary, sbuf):
    """default callback"""
    self.logger.info("pong default handler called!")
    print("pong default handler received: {0}".format(summary))
    self.rmr_free(sbuf)


xapp = RMRXapp(default_handler=defh, post_init=post_init, use_fake_sdl=True)
xapp.register_callback(sixtyh, GET_ACTION)
xapp.run()  # will not thread by default
