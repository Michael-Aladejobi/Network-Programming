import socket


server_socket = socket.socket(family = socket.AF_INET, type = socket.SOCK_STREAM)

print('Server Start: ')


port = 7000
ip = '127.0.0.1'

server_socket.bind((ip, port))
server_socket.listen(5)

con, addr = server_socket.accept()

print('Connected to Address: {0}, port no.:{1}'.format(addr[0], addr[1]))

data = con.recv(1024)
data = data.decode()

print('Message from client: ', data)