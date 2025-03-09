import socket

cs = socket.socket(family = socket.AF_INET, type = socket.SOCK_STREAM)

print('Client start: ')

port = 9000
ip = '127.0.0.1'

cs.connect((ip, port))

msg = input("Message to server: ")
cs.sendall(bytes(msg.encode('ascii')))

data = cs.recv(1024)
print('Message from server before decode: ', data)
data = data.decode()
print('Message from server after decode: ', data)

msg = input('Message to server: ')
while msg.lower().strip() != 'bye':
    cs.sendall(bytes(msg.encode('ascii')))
    data = cs.recv(1024)
    print('Messagr from server before decode: ', data)
    data = data.decode()
    print('Message from sever after decode: ', data)
    msg = input('Message to server or type (bye) to quit: ')
   
