# General Xapp 
Defination:
-----
    A general Xapp acts according to its own criteria
    (may include receipt of RMR messages).


This type of application is constricted by cerating a single while loop function. When function return a value the Xapp stops.
Therefore, Xapp must fetch its on data.

----
## Usage:

The framework only sets up an RMR thread and an SDL connection before invoking the client-provided function.


