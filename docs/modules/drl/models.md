# Models

Collection of network aritcture the actor will use to predict Q-value in given a state.

Each Class will be diffrent network aritcture, all class will implement __call__ 
funcation to bind fowrd to object as function.

----
<br>

## ActorNetwork:
    Simple 3 Fully connected articture
    with relu after each one
    with user activation function
<br>


## RecurrentNeuralNetwork:
    Reccurent network, 
    Will ube implement with GRU & LTSM

## ConvNetwork
    Will implement conv layer,
    as the model will get more data (will have droput and max pool)