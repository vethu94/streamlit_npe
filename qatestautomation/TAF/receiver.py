import json
import socket


s = socket.socket()
ip = socket.gethostbyname(socket.gethostname())
port = 12345

s.bind((ip, port))
s.listen(1)
conn, addr = s.accept()


data = conn.recv(1024).decode()
json_command = json.loads(data)

if json_command['action'] == 'print':
    print(json_command['message'])

conn.close()
