# _BaseXapp

Abstract class, should no be used.


    Parameters
        ----------
        rmr_port: int
            port to listen on

        rmr_wait_for_ready: bool (optional)

            if this is True, then init waits until rmr is ready to send, which
            includes having a valid routing file. This can be set to
            False if the client only wants to *receive only*.

        use_fake_sdl: bool (optional)
            if this is True, it uses dbaas' "fake dict backend" instead
            of Redis or other backends. Set this to true when developing
            your xapp or during unit testing to completely avoid needing
            a dbaas running or any network at all.

        post_init: function (optional)
            runs this user provided function after the base xapp is
            initialized; its signature should be post_init(self)

----
## API:
<br>

### _BaseXapp.rmr_get_messages:
    Return generator on all message from the qeue
    that as not been used by (read by) the client app.
    ####################################################
    Caller must free the memory after finish reading.

### _BaseXapp.rmr_send:
    Allocates a buffer, sets payload and mtype, and sends

### _BaseXapp.rmr_rts:
    Allows the xapp to return to sender, possibly adjusting the
    payload and message type before doing so. 
    #####################################################
    This does NOT free
    the sbuf for the caller as the caller may wish to perform
    multiple rts per buffer.

### _BaseXapp.rmr_free:
    Frees an rmr message buffer after use

### _BaseXapp.stop:
    cleans up and stops the xapp rmr thread (currently).
  