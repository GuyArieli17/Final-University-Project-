# Actors

Collection of Actors, will interact with the env.

_Actor is a base class interface.

----
<br>

## _Actor :
        Abstract class that create an actor, 
        with memory type and env 
- ### _exploration_action:
        Decide randomly to take radom action (Explore) or
        Determine one (Exploit)
- ### _take_one_step:
        Take on step in the environment.
        See the resualt of the action(step)
        And push to memory for future use
- ### train:
        How netork will be train.
        (each action , each batch-> gather inforamtion large 
        enough t then train)
- ### interact:
        one step in the ENV
<br>

---- 

## DQN :
        Deep Q-Network, approximates a state-value function in a Q-Learning         
        framework with a neural network.
        Implement the abstract Actor class

- ### interact:
        How we define interact with the environment.
        We do one action in a time 
- ### train:
        This function decide random action (explore| exploit)
        activate action and see delta information from env.
        And train the NN netwrok by mini batches
- ### train:
        How netork will be train.
        (each action , each batch-> gather inforamtion large enough t then train)
- ### interact:
        one step in the ENV
<br>