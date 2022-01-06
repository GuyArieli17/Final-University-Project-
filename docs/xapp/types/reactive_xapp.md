# Reactive Xapp 
Defination:
-----
    A reactive Xapp acts on messages that are delivered (pushed) via RMR. The Xapp --only-- takes action upon receipt of an RMR message.
-----



This type of application is constricted by cerating callback function and 
registering them with the framework by message type.
When a message is resived via RMR, the callback is invoked according to the message type ( each callback can be activated by diffrent message type). 

xApp must define defualt callback (handler), wich invoked when message arrives with no type-specific callback.

---
can be summary by exucate callback evrey time a message from type <T>
is arrived.