# Helper

Collection of extensions to the RMR base package

----
## API:
<br>

### Helper.rmr_rcvall_msgs:
    Assembles an array of all messages which can be received without blocking
    (but see the timeout parameter).  Effectively drains the message queue if
    RMR is started in mt-call mode, or draining any waiting TCP buffers.  If
    the pass_filter parameter is supplied, it is treated as one or more
    message types to accept (pass through). Using the default, an empty list,
    results in capturing all messages. If the timeout parameter is supplied
    and is not zero, this call may block up to that number of milliseconds
    waiting for a message to arrive. Using the default, ze

### Helper.rmr_rcvall_msgs_raw:
    Same as rmr_rcvall_msgs, but answers tuples with the raw sbuf.
    Useful if return-to-sender (rts) functions are required.
