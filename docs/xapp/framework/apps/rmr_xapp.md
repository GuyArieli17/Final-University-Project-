# RMR Xapp

Represents an Xapp that reacts only to RMR messages;
When get a message type call the function that been registed by the client.

    Parameters
    ----------
    default_handler: function
        A function with the signature (summary, sbuf) to be called
        when a message type is received for which no other handler is registered.
    default_handler argument summary: dict
        The RMR message summary, a dict of key-value pairs
    default_handler argument sbuf: ctypes c_void_p
        Pointer to an RMR message buffer. The user must call free on this when done.
    rmr_port: integer (optional, default is 4562)
        Initialize RMR to listen on this port
    rmr_wait_for_ready: boolean (optional, default is True)
        Wait for RMR to signal ready before starting the dispatch loop
    use_fake_sdl: boolean (optional, default is False)
        Use an in-memory store instead of the real SDL service
    post_init: function (optional, default None)
        Run this function after the app initializes and before the dispatch loop starts;
        its signature should be post_init(self)

----
## API:
<br>

### RMRXapp.register_callback:
    registers this xapp to call handler(summary, buf) when an rmr message is received of type message_type

### RMRXapp.run:
    This function should be called when the reactive Xapp is ready to start.
    After start, the Xapp's handlers will be called on received messages.

### RMRXapp.stop:
    cleans up and stops the xapp rmr thread (currently).
    [same as father]
  