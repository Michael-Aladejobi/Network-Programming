import socket

client_side = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)

port =9000
ip = '127.0.0.1'

client_side.connect((ip, port))

# msg = input('Message to Server: ')
# client_side.sendall(bytes(msg.encode('ascii')))

msg = input("Message to client: ")
while True:
    if msg == 'quit':
        print('Session Terminated by Client!')
        break
    else:
        client_side.sendall(bytes(msg.encode('ascii')))
        msg = input('Message Server or type "quit" to terminate: ')