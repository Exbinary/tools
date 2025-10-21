"""
<< Simple TCP HTTP client >>
Asks for host IP, Port and quantity of bytes desired as a response
Sends a raw HTTP/1.1 GET request to a given host and port using Python's socket API,
receives the full response, decodes and prints headers + body up to selected length. No external deps.
"""
import socket


targetHOST = input("Type target Host IP: ")
targetPORT = int(input("Type the Port: "))
lenghtOUT = int(input(f"How much bytes do you want to receive from {targetHOST}?: example:4096 :"))

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)   #Create a socket object


client.connect((targetHOST,targetPORT))       #Connect to the client   ------------

host_header = f"{targetHOST}:{targetPORT}"
Request = f"GET / HTTP/1.1\r\nHOST: {host_header}\r\n\r\n"   #Create the request

client.send(Request.encode('utf-8'))      #Send the request (encoded)

response = client.recv(lenghtOUT)        #Receive the response (up to choosen max bytes)

print(response.decode())

client.close()      #Close the connection   ----------------------------------------
