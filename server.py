import socket

ss = socket.socket(family=socket.AF_INT, type = socket.SOCK_DGRAM)
print('server start: ')

host = socket.gethostname()
port = 9999

ss.bind((host, port))

con,addr = ss.recvfrom(1024)
data = con.decode()
print('message from client: ', data)

msg = input('message to client: ')
msg = str.encode(msg)
ss.sendto(msg, (addr))

while True:
    con, addr = ss.recvfrom()
    data = con.decode()
    if not data:
        print('session ended')
        break
    if data.lower().strip() == 'bye':
        print('session terminated')
        break
    print('message from client: ')

    msg = input('message to server: ')
    msg = str.encode(msg)
    ss.sendto(msg, (addr))

