import socket

cs = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)
print('client start: ')

host = socket.gethostname()
port = 9000

cs.connect((host, port))

msg =input('message to server: ')
cs.sendall(bytes(msg.encode('ascii')))

data =cs.recv(1024).decode()
print('message from server: ', data)

msg = input('message to server: ')
while True:
    if msg.lower().strip() != 'bye':
        cs.sendall(bytes(msg.encode('ascii')))

        data = cs.recv(1024).decode()
        print('message from server: ', data)

        msg = input('message to server or type (bye) to quit: ')
    else:
        
        print('proces terminated!')
        break

cs.close()