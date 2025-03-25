import socket

cs = socket.socket( family = socket.AF_INET, type = socket.SOCK_DGRAM)


print('Client Start: ')

host = '127.0.0.1'
port = 7500

msg = input('Message to server--->: ')
msg = str.encode(msg)
cs.sendto(msg, (host, port))

con, addr = cs.recvfrom(1024)
data = con.decode()
print('Message from server after decoding:', data)

msg = input('Message to server--->: ')
msg = str.encode(msg)
cs.sendto(msg, (addr))