import socket


client_socket = socket.socket(family=socket.AF_INET, type = socket.SOCK_STREAM)

print('Client Start: ')

port = 7000
ip = '127.0.0.1'

client_socket.connect((ip, port))

msg = input('Message to server: ')
client_socket.sendall(bytes(msg.encode()))