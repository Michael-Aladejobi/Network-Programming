import socket
from _thread import *
import os

th = 0 #Thread counter var

def fun(ss2):
    pass

ss = socket.socket(family = socket.AF_INET, type = socket.SOCK_STREAM)

print('Server Start: ')
host = socket.gethostname()
port = 6000

ss.bind((host, port))
ss.listen(4)

while True:
    ss2, addr = ss.accept()
    print('Address client {0} and por no. {1}'.format(addr[0], addr[1]))
    start_new_thread(fun, (ss2,))

    th = th + 1 #client counter