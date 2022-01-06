# Memory

Collection of memory,

How we collet ad save data for future use.


----
<br>

## Experience :
        name tuple with all inforamtion given from gym.env 
----
<br>

## ReplayMemory:
        Class Determain how to save the data. \n
        Data will be save in ndarray with fix size. \n
        When the array is fill we will replace the oldes data \n
        (FIFO)
- ### push:
        push list of data point into memory
- ### sample:
        Randomly pick batch from memory
<br>

