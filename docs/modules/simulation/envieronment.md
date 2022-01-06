# Envieronment

This class Environment,
    The env present all the action we can do.
    according to gym.ENV API DOC: https://gym.openai.com/docs/

----
<br>

- ### reset:
        The function will reset the simulation and return the last state
- ### _after_action_cool_down:
        Will frezee all lights 
        Untill the freeze time is up.
        (created to prevent situation where there is a car
        in the intersection, and the other lights will hace
        a green light)
- ### step:
        Get action from user and activate this functio in 
        the simulation return inforamtuion as a tuple
- ### stochastic:
        stochastic implemntation in the ENV 
- ### set_action:
        Get action (index of phase in intersection flow file - we wrote beffore running)
        and activate the function in the simulator(cityflow)

<br>

