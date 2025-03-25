import socket

cs = socket.socket( family = socket.AT_INET, type = socket.SOCK_DGRAM)


print('Client Start: ')

host = '127.0.0.1'
port = 7500

msg = input('Message to server--->: ')
msg = str.encode(msg)
cs.sendto(msg, (host, port))