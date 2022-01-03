# Xapp

Represents a generic Xapp where the client provides a function for the framework to call,
which usually contains a loop-forever construct.

    Parameters
    ----------
    entrypoint: function
        This function is called when the Xapp class's run method is invoked.
        The function signature must be just function(self)
    rmr_port: integer (optional, default is 4562)
        Initialize RMR to listen on this port
    rmr_wait_for_ready: boolean (optional, default is True)
        Wait for RMR to signal ready before starting the dispatch loop
    use_fake_sdl: boolean (optional, default is False)
        Use an in-memory store instead of the real SDL service

----
## API:
<br>

### RMRXapp.run:
    This function should be called when the general Xapp is ready to start.