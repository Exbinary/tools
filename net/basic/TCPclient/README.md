
Simple TCP client that outputs a HTTP response to given IP:Port

Asks for host IP, Port and quantity of bytes desired as a response
Sends a raw HTTP/1.1 GET request to a given host and port using Python's socket API,
receives the full response, decodes and prints headers + body up to selected length. No external dep.

[Usage] > python3 TCPclient.py
