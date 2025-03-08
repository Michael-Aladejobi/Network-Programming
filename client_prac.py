import socket

client_side = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)

port =9000
ip = '127.0.0.1'

client_side.connect((ip, port))

# msg = input('Message to Server: ')
# client_side.sendall(bytes(msg.encode('ascii')))