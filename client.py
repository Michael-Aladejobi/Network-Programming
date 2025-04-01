import socket

cs = socket.socket(family = socket.AF_INET, type = socket.SOCK_STREAM)

print('Client Strat: ')

host = '127.0.0.1'
port = 6000

cs.connect((host, port))

msg = input('message to server: ')
cs.sendall(msg.encode('ascii'))

data = cs.recv(1024).decode()
print('message from server: ', data)

