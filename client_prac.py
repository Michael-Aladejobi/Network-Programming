import socket

cs = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)

print('Client Start: ')

port = 9000
ip = '127.0.0.1'

cs.connect((ip, port))

msg = input('Message to server: ')
while True:
    if msg.lower().strip() == 'quit':
        print('session Ended from client!')
        break
    cs.sendall(bytes(msg.encode('ascii')))
    msg = input('Message to server: ')