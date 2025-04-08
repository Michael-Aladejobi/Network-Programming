import socket
from _thread import *
import os

th = 0 #thread var counter

def func(con):
    data = con.recv(1024).decode()
    print('message from client: ', data)

    msg = input('mesage to client: ')
    while True:
        if msg.lower().strip() != 'bye':
            con.sendall(msg.encode('ascii'))

            data = con.recv(1024).decode()
            print('message from client: ', data)

            msg = input('message to client: ')


print('server start: ')

ss = socket.socket(family=socket.AF_INET, type = socket.SOCK_STREAM)

host = socket.gethostname()
port = 9999

ss.bind((host, port))
ss.listen(5)

while True:
    con, addr = ss.accept()
    print('Connected to addr {0}, port no. {1}'.format(addr[0], addr[1]))

    start_new_thread(func,(con,))
    th = th + 1
    print('thread no.: ', th)

    print('process id: '.format(os.getpid()))
