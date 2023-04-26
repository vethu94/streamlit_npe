import json
import socket

s = socket.socket()
ip = '192.168.1.2'
port = 12345

s.connect((ip, port))

command = {'action': 'print', 'message': 'Heyy'}

json_command = json.dumps(command)

s.sendall(json_command.encode())

s.close()
