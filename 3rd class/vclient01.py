import socket

cs = socket.socket(family = socket.AF_INET, type = socket.SOCK_STREAM)

print('Client Start: ')

host = socket.gethostname()
port = 7500

cs.connect((host, port))

msg = input('Message to server: ')
cs.sendall(bytes(msg.encode('ascii')))

data = cs.recv(1024).decode()
print('Message from server: ', data)

msg = input('Message to server: ')

while msg.lower() != 'bye':
    cs.sendall(bytes(msg.encode('ascii')))

    data = cs.recv(1024).decode()
    print('Message from server: ', data)

    data = cs.recv(1024).decode()
    print('Message from server: ', data)

    msg = input('Message 1 - 9 to server or type bye to quit: ')

cs.close()
print('Client close')