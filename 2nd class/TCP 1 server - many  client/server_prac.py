import socket
from _thread import *
import os

th = 0

def func(con):
    data = con.recv(1024).decode()
    print('message from client: ', data)

    msg = input('message to client: ')
    con.sendall(bytes(msg.encode('ascii')))

    while True:
        data = con.recv(1024).decode()
        if not data:
            print('session ended')
            break
        if data.lower().strip():
            print('session ended')
        print('message from client: ', data)

        msg  = input('message to client: ')
        con.sendall(bytes(msg.encode('ascii')))

ss = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)
print('server start: ')

host = socket.gethostname()
port = 6000
ss.bind((host, port))
ss.listen(5)

while True:
    con, addr = ss.accept()
    print(f'Connected to Address: {addr[0]}, port no: {addr[1]}')

    start_new_thread(func, (con,))
    
    th = th + 1
    print('Thread no: ', th)
    print(f'Process ID: {format(os.getpid())}')