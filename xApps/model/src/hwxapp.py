# ==================================================================================
#
#       Copyright (c) 2020 Samsung Electronics Co., Ltd. All Rights Reserved.
#
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#          http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.
#
# ==================================================================================

from os import getenv
from ricxappframe.xapp_frame import RMRXapp, rmr


from .utils.constants import Constants
from .manager import *

from .handler import *
from mdclogpy import Logger

import torch as th
from torch import nn

class ActorNetwork(nn.Module):
    """
    A network for actor
    """
    def __init__(self, state_dim, hidden_size, output_size, output_act):
        super(ActorNetwork, self).__init__()
        self.fc1 = nn.Linear(state_dim, hidden_size)
        self.fc2 = nn.Linear(hidden_size, hidden_size)
        self.fc3 = nn.Linear(hidden_size, output_size)
        self.output_act = output_act

    def forward(self, state):
        out = nn.functional.relu(self.fc1(state))
        out = nn.functional.relu(self.fc2(out))
        out = self.output_act(self.fc3(out))
        return out


ACTION_DIM = 8
STATE_DIM = 24
HIDDEN_LAYER = 50

def init__dqn_model():
    model = ActorNetwork(STATE_DIM, HIDDEN_LAYER, ACTION_DIM, nn.ReLU())
    model.load_state_dict(th.load('model.pth'))
    optimizer = th.optim.Adam(self._model.parameters())
    
    return model, optimizer

class HWXapp:

    def __init__(self):
        fake_sdl = getenv("USE_FAKE_SDL", False)
        self._rmr_xapp = RMRXapp(self._default_handler,
                                 config_handler=self._handle_config_change,
                                 rmr_port=4560,
                                 post_init=self._post_init,
                                 use_fake_sdl=bool(fake_sdl))
                                 
        self._model, self._optimizer = init__dqn_model()
        
        # Print model's state_dict
        print("Model's state_dict:")
        for param_tensor in self._model.state_dict():
            print(param_tensor, "\t", self._model.state_dict()[param_tensor].size())
        
        # Print optimizer's state_dict
        print("Optimizer's state_dict:")
        for var_name in self._optimizer.state_dict():
            print(var_name, "\t", self._optimizer.state_dict()[var_name])
        

    def _post_init(self, rmr_xapp):
        """
        Function that runs when xapp initialization is complete
        """
        rmr_xapp.logger.info("HWXapp.post_init :: post_init called")
        # self.sdl_alarm_mgr = SdlAlarmManager()
        # sdl_mgr = SdlManager(rmr_xapp)
        # sdl_mgr.sdlGetGnbList()
        # a1_mgr = A1PolicyManager(rmr_xapp)
        # a1_mgr.startup()
        # sub_mgr = SubscriptionManager(rmr_xapp)
        # enb_list = sub_mgr.get_enb_list()
        # for enb in enb_list:
            # sub_mgr.send_subscription_request(enb)
        # gnb_list = sub_mgr.get_gnb_list()
        # for gnb in gnb_list:
            # sub_mgr.send_subscription_request(gnb)
        # metric_mgr = MetricManager(rmr_xapp)
        # metric_mgr.send_metric()

    def _handle_config_change(self, rmr_xapp, config):
        """
        Function that runs at start and on every configuration file change.
        """
        rmr_xapp.logger.info("HWXapp.handle_config_change:: config: {}".format(config))
        rmr_xapp.config = config  # No mutex required due to GIL

    def _default_handler(self, rmr_xapp, summary, sbuf):
        """
        Function that processes messages for which no handler is defined
        """
        rmr_xapp.logger.info("HWXapp.default_handler called for msg type = " +
                                   str(summary[rmr.RMR_MS_MSG_TYPE]))
        rmr_xapp.rmr_free(sbuf)

    def createHandlers(self):
        """
        Function that creates all the handlers for RMR Messages
        """
        HealthCheckHandler(self._rmr_xapp, Constants.RIC_HEALTH_CHECK_REQ)
        A1PolicyHandler(self._rmr_xapp, Constants.A1_POLICY_REQ)
        SubscriptionHandler(self._rmr_xapp,Constants.SUBSCRIPTION_REQ)

    def start(self, thread=False):
        """
        This is a convenience function that allows this xapp to run in Docker
        for "real" (no thread, real SDL), but also easily modified for unit testing
        (e.g., use_fake_sdl). The defaults for this function are for the Dockerized xapp.
        """
        self.createHandlers()
        self._rmr_xapp.run(thread)

    def stop(self):
        """
        can only be called if thread=True when started
        TODO: could we register a signal handler for Docker SIGTERM that calls this?
        """
        self._rmr_xapp.stop()
