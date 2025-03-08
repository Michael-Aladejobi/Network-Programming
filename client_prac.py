import socket

cs = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)

print('Client Start: ')

port = 9000
ip = '127.0.0.1'

cs.connect((ip, port))
