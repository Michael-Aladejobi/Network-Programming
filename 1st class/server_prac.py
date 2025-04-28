import socket
import time

ss = socket.socket(family=socket.AF_INET, type = socket.SOCK_STREAM)
print('server start: ')

host = '127.0.0.1'
port = 6000

ss.bind((host, port))
ss.listen(5)

con, addr = ss.accept()
print('Connected to Address: {0}, port no.: {1}'.format(addr[0], addr[1]))

data = con.recv(1024).decode()
print('message from server: ', data)

msg = input('message to client: ')
con.sendall(bytes(msg.encode()))

data = con.recv(1024).decode()
while True:
    if not data:
        print('no data from client!')
        break
    if data.lower().strip() == 'bye':
        print('session ended by client')
        break
    print('message from client: ', data)

    msg = time.ctime(time.time())
    con.sendall(bytes(msg.encode('ascii')))
    

    data = con.recv(1024)

ss.close()