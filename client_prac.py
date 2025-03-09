import socket
cs = socket.socket(family=socket.AF_INET, type = socket.SOCK_STREAM)

print('Client start: ')

port = 9000
ip = '127.0.0.1'

cs.connect((ip, port))

msg = input('Message to serer: ')
cs.sendall(bytes(msg.encode('ascii')))

data = cs.recv(1024)
print('Message from server before decode: ', data)

data = data.decode()
print('Message from server after decode: ', data)

msg = input('Message to server: ')
while True:
    if msg.upper() == 'QUIT':
        print('Session ended by Client!')
        break
    else:
        cs.sendall(bytes(msg.encode('ascii')))
        data = cs.recv(1024).decode()
        print('Message recv from server: ', data)
        msg = input('Message to server: ')


