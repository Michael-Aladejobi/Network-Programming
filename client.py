import socket

cs = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)
print('client start: ')

host = socket.gethostname()
port = 9999

msg = input('message to server: ')
msg = str.encode(msg)
cs.sendto(msg, (host, port))

con, addr = cs.recvfrom(1024)
data = con.decode()
print('messqge from server: ', data)

msg = input('message to server as a _ b _ c: ')
msg = str.encode(msg)
cs.sendto(msg, (host, port))

con, addr = cs.recvfrom(1024)
data = con.decode()
print('message from server: ', data)