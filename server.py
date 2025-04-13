import socket
import calendar

ss = socket.socket(family=socket.AF_INET,type=socket.SOCK_DGRAM)
print('server start: ')

host = socket.gethostname()
port = 9999

ss.bind((host, port))
con, addr = ss.recvfrom(1024)

print('Connected to addr: {0}'.format(addr))

data = con.decode()
print('message from client: ', data)

msg = input('message to client: ')
msg = str.encode(msg)
ss.sendto(msg, (addr))

while True:
    con, addr = ss.recvfrom(1024)
    data = con.decode()
    print('message from client: ', data)