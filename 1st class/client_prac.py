import socket

cs = socket.socket(family = socket.AF_INET, type = socket.SOCK_STREAM)
print('Client start: ')

host = socket.gethostname()
port = 6000

cs.connect((host, port))

msg = input('message to server: ')
cs.sendall(bytes(msg.encode('ascii')))

data = cs.recv(1024)
print('message from server b/f decoding: ', data)
data = data.decode()
print('message from server after decoding: ', data)


msg = input('message to server: ')
while True:
    if msg.lower().strip() != 'bye':
        cs.sendall(bytes(msg.encode('ascii')))
    else:
        print('session ended')
        break
    data = cs.recv(1024).decode()
    print('message from server: ', data)

    msg = input('message to server or type (bye) to quit: ')