import socket

cs = socket.socket(family=socket.AF_INET, type = socket.SOCK_DGRAM)
print('Client start: ')

host = "127.0.0.1"
port = 6000

msg = input('message to server: ')
msg = str.encode(msg)
cs.sendto(msg, (host,port))

con, addr = cs.recvfrom(1024).decode()
print('message from server: ', con.decode())