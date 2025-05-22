import socket
import time

ss = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print('Server start: ')

host = '127.0.0.1'
port = 6000

ss.bind((host, port))
ss.listen(5)

con, addr = ss.accept()
print('Connected to addr : {0}, port: {1}'.format(addr[0], addr[1]))

data = con.recv(1024)
print('msg from client b/f decoding: ', data)
data = data.decode()
print('msg from client a/f decoding: ', data)

msg = input(' message to client: ')
msg = msg.encode('ascii')
con.sendall(bytes(msg))

while True:
    data = con.recv(1024)
    if not data:
        print('end time request')
        break
    if data.lower().strip() == 'bye':
        print('end time request')
        break
    print('message from client: ', data)

    msg = time.ctime(time.time())
    con.sendall(bytes(msg.encode('ascii')))