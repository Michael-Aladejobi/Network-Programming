import socket


cs = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)
print('Client start: ')
host = socket.gethostname()
port = 3000
cs.connect((host, port))
msg = input('message to server : ')
cs.send(bytes(msg.encode('ascii')))

data = cs.recv(1024).decode()
print('message from server : ',data)

msg = input('message to server : ')
while msg.lower() != 'bye':

    cs.send(bytes(msg.encode('ascii')))

    data = cs.recv(1024).decode()
    print('message from server : ',data)

    data = cs.recv(1024).decode()
    print('message from server : ',data)
    msg = input('message 1 to 9 to server or type (bye) to quit : ')
cs.close()