import socket

ss = socket.socket( family = socket.AT_INET, type = socket.SOCK_DGRAM)


print('Server Start: ')

host = '127.0.0.1'
port = 7500

#UDP doesnt listen and doesnt , hence...
ss.bind((host, port))

#UDP recev from and send to
con, addr = ss.recvfrom(1024)

print('Add')