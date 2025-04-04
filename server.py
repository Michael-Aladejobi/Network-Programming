import socket
from _thread import *
import os

th = 0 #thread counter

def func(c):
    data = c.recv(1024).decode()
    print('meaasage from client: ', data)

ss = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)

print('server start: ')

host = socket.gethostname()
port = 7000

ss.bind((host, port))
ss.listen(5)

while True:
    con, addr = ss.accept()
    print('connected to addr {0}, port no. {1}'.format(addr[0], addr[1]))

    start_new_thread(func, (con,))
    th = th + 1
    print('thread no.: ', th)

    print('process id: {}'.format(os.getpid()))