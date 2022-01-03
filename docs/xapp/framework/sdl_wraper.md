# SDLWrapper

Wrapper around Python SDL interface.

    Parameters
        ----------
        use_fake_sdl: bool (optional, default False)
            if this is True, then use SDL's in-memory backend,
            which is very useful for testing since it allows use
            of SDL without a running SDL or Redis instance.
            This can be used while developing an xapp and also
            for monkeypatching during unit testing; e.g., the xapp
            framework unit tests do this.

----
## API:
<br>

### SDLWrapper.set:
    Stores a key-value pair,
    optionally serializing the value to bytes using msgpack.

### SDLWrapper.get:
    Gets the value for the specified namespace and key,
    optionally deserializing stored bytes using msgpack.

### SDLWrapper.find_and_get:
    Gets all key-value pairs in the specified namespace
    with keys that start with the specified prefix,
    optionally deserializing stored bytes using msgpack.
    
### SDLWrapper.delete:
    Deletes the key-value pair with the specified key in the specified namespace.

-----
All this function is been used by Xapp