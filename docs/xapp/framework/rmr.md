# RMR

Wraps all RMR functions, but does not have a reference to the shared library.


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

### RMR.rmr_mbuf_t:
      Mirrors public members of type rmr_mbuf_t from RMR header file src/common/include/rmr.h

### RMR.rmr_init:
    Prepares the environment for sending and receiving messages.
    Refer to RMR C documentation for method::extern void* rmr_init(char* uproto_port, int max_msg_size, int flags)
    This function raises an exception if the returned context is None.

### RMR.rmr_ready:
    Checks if a routing table has been received and installed.
    Refer to RMR C documentation for method::extern int rmr_ready(void* vctx)

### RMR.rmr_close:
    Closes the listen socket.
    Refer to RMR C documentation for method::extern void rmr_close(void* vctx)

---
<br/>
### MORE FUNCTION BEEN USE TO BIND TO PYTHON CPP
<br/><br/>

----
## Const: (not implementit!!!)
-----
    #Publish keys used in the message summary dict as constants
    message payload, bytes
    RMR_MS_PAYLOAD = "payload"
    # payload length, integer
    RMR_MS_PAYLOAD_LEN = "payload length"
    # message type, integer
    RMR_MS_MSG_TYPE = "message type"
    # subscription ID, integer
    RMR_MS_SUB_ID = "subscription id"
    # transaction ID, bytes
    RMR_MS_TRN_ID = "transaction id"
    # state of message processing, integer; e.g., 0
    RMR_MS_MSG_STATE = "message state"
    # state of message processing converted to string; e.g., RMR_OK
    RMR_MS_MSG_STATUS = "message status"
    # number of bytes usable in the payload, integer
    RMR_MS_PAYLOAD_MAX = "payload max size"
    # managed entity ID, bytes
    RMR_MS_MEID = "meid"
    # message source, string; e.g., host:port
    RMR_MS_MSG_SOURCE = "message source"
    # transport state, integer
    RMR_MS_ERRNO = "errno"