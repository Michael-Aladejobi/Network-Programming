import socket

cs = socket.socket(family = socket.AF_INET, type = socket.SOCK_STREAM)
print('client start: ')

port = 9001
ip = '127.0.0.1'
cs.connect((ip, port))


# sending msg to server using TCP 
msg = input('message to server: ')
cs.sendall(bytes(msg.encode('ascii')))

data = cs.recv(1024).decode()
print('message from server ', data)

msg = input('message to server: ')
while msg.lower().strip() != 'bye':
    cs.sendall(bytes(msg.encode('ascii')))
    data = cs.recv(1024).decode()
    print('message from server ', data)
    msg = input('message time or type (bye) to quit: ')
