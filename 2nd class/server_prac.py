import socket
from _thread import *
import os

th = 0

def func(con):
    data = con.recv(1024).decode()
    print('meaage from client: ', data)

ss = socket.socket(family=socket.AF_INET, type = socket.SOCK_STREAM)
print('Server start: ')

host = '127.0.0.1'
port = 9000

ss.bind((host, port))
ss.listen(5)

while True:
    con, addr = ss.accept()
    print('Connected to addr: {0}, port: {1}'.format(addr[0], addr[1]))
    start_new_thread(func,(con,))

    th = th + 1
    print('thread no: ', th)
    print('Process id: {0}'.format(os.getpid()))