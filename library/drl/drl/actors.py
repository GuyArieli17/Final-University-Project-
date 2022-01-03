# ==================================================================================
#       Copyright (c) 2019-2022 Guy Arieli (GuyArieli17)
#       Copyright (c) 2018-2020 Eran
#       Copyright (c) 2018-2020 Amit
#
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
# ==================================================================================
from .memory import ReplayMemory, Experience
from abc import abstractmethod
import torch as th
import numpy as np

# ________________ Actor ________________
class Actor:
    """
        Abstract class that create an actor, 
        with memory type and env 
    """

    ###############
    # PRIVATE API #
    ###############

    # class constructor
    def __init__(self, memory_size, network, env, epsilon_start, epsilon_end,
                 action_dim, epsilon_decay, loss_fnc, actor_optimizer, gamma,max_steps,done_penalty,batch_size):
        """
            Init funation
            @Params
            --------
            memory_size: 
                the size of memory(fixed size)
            network:
                the NN model articture 
            env:
                environment of which we running on. (implemnt gym api)
            epsilon_start:
                epsilon we start from
            epsilon_end:
                the minimum value of epsilon we can get
            action_dim:
                the dimension of the action space
            epsilon_decay:
                how fast the epsilon value change(decay)
            loss_fnc:
                function on which we decide  what action to take( the loss function of nn)
            actor_optimizer:
                the optimizer for the model
            gamma:
                disscount factor for future outcome
            max_steps:
                max step in each iteration
            done_penalty:
                what penalty we get when we finish 
            batch_size:
                the size on wich we train the data
        """
        self.memory = ReplayMemory(memory_size)
        self.network = network
        self.env = env
        self.epsilon_start = epsilon_start
        self.epsilon_end = epsilon_end
        self.epsilon_decay = epsilon_decay
        self.action_dim = action_dim
        self.loss_function = loss_fnc
        self.actor_optimizer = actor_optimizer
        self.gamma = gamma
        self.current_state = env.reset()
        self.n_steps = 1
        self.max_steps = max_steps
        self.done_penalty = done_penalty
        self.n_episodes = 0
        self.batch_size = batch_size
    
    # choose an action based on state with random noise added for exploration in training
    def _exploration_action(self, state):
        """
            Decide randomly to take radom action (Explore) or
            Determine one (Exploit)

            @Params
            -------
            state:
                state in current time
            -------

            @Return
            -------
            the action we should take
            -------
        """
        # calc epsilon 
        epsilon = self.epsilon_end + (self.epsilon_start - self.epsilon_end) * \
                  np.exp(-1. * self.n_steps / self.epsilon_decay)
        # decide randomly which action to take
        if np.random.rand() < epsilon:
            rnd_action = np.random.choice(self.action_dim)
            return rnd_action
        # chose the exploit
        learned_action = th.argmax(self.network(th.tensor(state).float()))
        return learned_action

    # do one step in world (without train do one step and push to memory)
    def _take_one_step(self):
        """
            Take on step in the environment.
            See the resualt of the action(step)
            And push to memory for future use
        """
        # get crrent information
        state = self.current_state
        action = self._exploration_action(self.current_state)
        # do step in env
        next_state, reward, done, _ = self.env.step(action)
        # check if finish or pass max steps
        if done and (self.n_steps >= self.max_steps):
            reward = self.done_penalty
            next_state = np.zeros(len(state))
            self.n_steps = 0
            self.current_state = self.env.reset()
            self.n_episodes += 1
            self.episode_done = True
        else: 
            # can continue
            self.current_state = next_state
            self.episode_done = False
        # update number of states and push to memory
        self.n_steps += 1
        self.memory.push(state, action, reward, next_state, done)

    ##############
    # PUBLIC API #
    ##############

    @abstractmethod
    # run actor inside the environment
    def train(self):
        """
            The Function decide how we train the model 
            Child instance have to implement this function
        """
        NotImplementedError("Need to Implement In Sub Class")

    
    @abstractmethod
    # do only steps don't learn(eval)
    def interact(self):
        """
            The Function decide how the actor interact with the 
            environment
            ----------
            Child instance have to implement this function
        """
        NotImplementedError("Need to Implement In Sub Class")

# ________________ DQN ________________
class DQN(Actor):

    """
        Deep Q-Network, approximates a state-value function in a Q-Learning framework with a neural network.
        Implement the abstract Actor class
    """

    ###############
    # PRIVATE API #
    ###############

    # class constructor
    def __init__(self, memory_size, network, env, epsilon_start, epsilon_end,
                 action_dim, epsilon_decay, loss_fnc, actor_optimizer, gamma, max_steps, done_penalty, batch_size):
        """
            Init funation
            @Params
            --------
            memory_size: 
                the size of memory(fixed size)
            network:
                the NN model articture 
            env:
                environment of which we running on. (implemnt gym api)
            epsilon_start:
                epsilon we start from
            epsilon_end:
                the minimum value of epsilon we can get
            action_dim:
                the dimension of the action space
            epsilon_decay:
                how fast the epsilon value change(decay)
            loss_fnc:
                function on which we decide  what action to take( the loss function of nn)
            actor_optimizer:
                the optimizer for the model
            gamma:
                disscount factor for future outcome
            max_steps:
                max step in each iteration
            done_penalty:
                what penalty we get when we finish 
            batch_size:
                the size on wich we train the data
        """
        super(DQN, self).__init__(memory_size, network, env, epsilon_start, epsilon_end, action_dim, epsilon_decay,
                                  loss_fnc, actor_optimizer, gamma, max_steps, done_penalty, batch_size)
    
    # do a train to the network with random bath from memory
    def _train_mini_batch(self, mini_batch):
        """
            TODO: Check and determine the size of each input

            @Params
            -------
            mini_batch: 
                numpy_ndarray that include all sample to train on
        """
        # init all tensor size
        done_tensor = th.zeros(*mini_batch.shape[:-1])
        reward_tensor = th.zeros(*mini_batch.shape[:-1])
        current_states_tensor = th.zeros((*mini_batch.shape[:-1], *self.current_state.shape))
        next_states_tensor = th.zeros((*mini_batch.shape[:-1], *self.current_state.shape))
        #  run on all data points (expireince)
        for idx, exp in enumerate(mini_batch):
            exp_state, exp_action, exp_reward, exp_new_state, exp_done = list(
                    map(lambda val: th.tensor(val).float(), [*exp]))
            done_tensor[idx] = exp_done
            current_states_tensor[idx] = exp_state
            reward_tensor[idx] = exp_reward
            next_states_tensor[idx] = exp_new_state
        # remove pass gradient
        self.actor_optimizer.zero_grad()
        prediction = self.network(current_states_tensor)
        prediction_next = self.network(next_states_tensor)
        # get the index of the best action(in last position)
        best_action_indexes = th.argmax(prediction, dim=-1)
        best_action_indexes_next = th.argmax(prediction_next, dim=-1)
        # select for each state best q-value
        current_state_predictions = prediction[:, :, best_action_indexes]
        current_state_predictions_next = prediction_next[:, :, best_action_indexes_next]
        # crete lables
        labels = reward_tensor + th.logical_not(done_tensor) * (self.gamma * current_state_predictions_next)
        loss = self.loss_function(labels, current_state_predictions)
        loss.backward()
        self.actor_optimizer.step()
    
    ##############
    # PUBLIC API #
    ##############

    # do interaction with the world (insert to memory)
    def interact(self):
        """
            How we define interact with the environment.
            We do one action in a time 
        """
        super(DQN, self)._take_one_step()

    # make a step and train network
    def train(self):
        """
            This function decide random action (explore| exploit)
            activate action and see delta information from env.
            And train the NN netwrok by mini batches
        """
        # decide which action to take
        action = self._exploration_action([self.current_state])
        # save data from env
        current_state = self.current_state
        # implement action in env & get information
        new_state, reward, done, _ = self.env.step(action)
        # convert to tensors
        new_state = th.tensor(new_state).float()
        reward = th.tensor(reward).float()
        done = th.tensor(done).float()
        # append to buffer memory
        self.memory.push(current_state, th.tensor(action).float(), reward, new_state, done)
        # Choose random batchf from memory
        mini_batch = self.memory.sample(self.batch_size)
        mini_batch = np.array(mini_batch)
        # train minibatch
        self._train_mini_batch(mini_batch)










