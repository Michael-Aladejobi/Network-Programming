import socket

cs = socket.socket(family = socket.AF_INET, type = socket.SOCK_STREAM)

print('Client Start: ')

host = socket.gethostname()
port = 7000

cs.connect((host, port))

msg = input('Message to server: ')
cs.sendall(bytes(msg.encode('ascii')))

data = cs.recv(1024).decode()
print('Message from server: ', data)

msg = input('Message to server: ')
cs.sendall(bytes(msg.encode('ascii')))

data = cs.recv(1024).decode()
print('Message from server: ', data)

data = cs.recv(1024).decode()
print('Message from server: ', data)