import socket

cs = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)

print('client start: ')

host = socket.gethostname()
port = 7000
cs.connect((host, port))

msg = input('message to server: ')
cs.sendall(bytes(msg.encode('ascii')))