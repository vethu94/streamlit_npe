import socket
import json


# Define the IP address and port number of the receiving machine
ip_address = '192.168.22.80'
port = 12345

# Create a socket object and connect to the receiving machine
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((ip_address, port))

# Create the JSON string that you want to send
data = {'message':'Test_Power'}
json_string = json.dumps(data)

# Send the JSON string over the socket connection
sock.sendall(json_string.encode())

# Close the socket connection
sock.close()