# IPC
Simple Project-Specific Inter-process Communication Library

#[DRAFT] Classes
TODO: replace with pydoc once code is written
##Private

```_socket_ipc_connection```

```_unix_socket_ipc_connection```
##Public
###Core Classes
```socket_ipc_factory```
        
        Generates connections to remote programs.

        Public Methods/Public Variables:
```     
        endpoints
```
        
                Enum mapped to socket endpoint names (i.e. hostname:port or unix socket path)

```     
        get_connection(endpoint)
```
        
                Factory method that returns a socket connection object

```socket_ipc_connection```
        
        Socket connection object, returned by ipc factory class. Subclasses will be specific to the connection target.
        
        Public Methods/Public Variables:

```
        init()
```
```
        is_open()
```

```
        read_next()
```
```
        read_front()
```
```
        write(message_object)
```
```
        close()
```
####Message Objects
```vehicle_state```

```radio_state```

```log_event```

```belief_update```

```belief_grid```
