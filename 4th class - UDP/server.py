import socket

ss = socket.socket( family = socket.AF_INET, type = socket.SOCK_DGRAM)


print('Server Start: ')

host = '127.0.0.1'
port = 7500

#UDP doesnt listen and doesnt , hence...
ss.bind((host, port))

#UDP recev from and send to
con, addr = ss.recvfrom(1024)

print('Address client connected %s: ' % str(addr))
print('Message from client before decoding: ',  con)

data = con.decode()
print('Message from client after decoding:', data)

msg = input('Message to client--->: ')
msg = str.encode(msg)
ss.sendto(msg, (addr))

con, addr = ss.recvfrom(1024)
data = con.decode()
print('Message from client after decoding: ', data)