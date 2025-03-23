import socket

cs = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)

print('Client Start: ')
port = 9000
host = '127.0.0.1'

cs.connect((host, port))

msg = input('message to server: ')
cs.sendall(bytes(msg.encode('ascii')))

data = cs.recv(1024).decode()
print('message from server: ',data)

msg = input('message to server: ')
while msg.lower() != 'quit':
    cs.sendall(bytes(msg.encode('ascii')))
    data = cs.recv(1024).decode()
    print('message from server: ', data)
    msg = input('message to server: ')