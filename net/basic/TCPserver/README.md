This Python script creates a basic multi-threaded TCP server that listens on given Port.
It accepts incoming client connections, spawns a new thread for each client, receives a message (up to 1024 bytes), prints it, and sends back a simple acknowledgment ('ACK').
