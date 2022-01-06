# CityFlow API

This class is abstraction of CityFlowAPI: https://cityflow.readthedocs.io/en/latest/start.html#data-access-api

It's easy to maintain and change withput a need to update the rest of the code

----
<br>

- ### push:
        Get all data from simulation and reorganize 
        it, remove the unnecessary data and preforme some
        function to clean the data. 
- ### reset:
        reset connected ENV
- ### next_frame:
        set nect frame in ENV
- ### stochastic:
        stochastic implemntation in the ENV 
- ### set_action:
        Get action (index of phase in intersection flow file - we wrote beffore running)
        and activate the function in the simulator(cityflow)

<br>

