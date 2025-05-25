import socket
import os
from _thread import *


th  = 0

def func(con):
    while True:
        msg = input('message to client: ')
        con.sendall(bytes(msg.encode('ascii')))

        data = con.recv(1024).decode()
        if not data or data.lower().strip() == 'bye':
            print('Game ended')
            break
        print('message from client :', data)

ss = socket.socket(family=socket.AF_INET, type = socket.SOCK_STREAM)
print('Server Strted: ')

host = '127.0.0.1'
port = 6000

ss.bind((host, port))
ss.listen(5)

while True:
    con, addr = ss.accept()
    print('Connected to addr {0}, port {1}'.format(addr[0], addr[1]))

    start_new_thread(func, (con,))

    th = th + 1
    print('Thread no: ', th)

    print('Process ID: '.format(os.getpid()))

