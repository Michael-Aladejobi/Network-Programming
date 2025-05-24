import socket
import time

ss = socket.socket(family = socket.AF_INET, type = socket.SOCK_STREAM)
print('server start: ')

# Assigning port numbers.........

port = 9001
ip = '127.0.0.1'
ss.bind((ip, port))
ss.listen(2) # the 2 here is the number of client the server will listen to at the same time maximum is 5
con, addr = ss.accept()
print('address client connected {0} and port number {1}'.format(addr[0], addr[1]))

data = con.recv(2020)
print('message from client before decoding: ', data)

data = data.decode()
print('message from client after decoding: ', data)

msg = input('message to client: ')
con.sendall(bytes(msg.encode('ascii')))

while True:
    data = con.recv(2020).decode()
    if not data:
        print('end time request')
        break
    print('message from client: ', data)
    mg = time.ctime(time.time())+'\r\n'
    con.sendall(bytes(mg.encode('ascii')))
