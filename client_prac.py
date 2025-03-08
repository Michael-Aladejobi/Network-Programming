import socket


clientSide = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)

print('Client Ready: ')

port = 9000
ip = '127.0.0.1'

clientSide.connect((ip, port))

msg = input('Message to server: ')

while True:
    if msg.lower() == 'quit':
        print('Session terminated by client!') 
        break
    else:
        clientSide.sendall(bytes(msg.encode('ascii')))
        msg = input('Message to server: ')
        
