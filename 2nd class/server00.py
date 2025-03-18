# Server_client Thread

import socket 
from _thread import *
import os

th = 0

ss = socket.socket(family=socket.AF_INET, type = socket.SOCK_STREAM)
print("Start Server: ")

host = '127.0.0.1'
port = 9000;


host = socket.grthostname()
port = 8500
ss.bind((host , port))
ss.listen(5)

while True:
    con, addr = ss.accept()
    print("sddress client conn. {} and port no. {}".format (addr[0], addr[1]))
    start_new_thread{func, (con,))

    th = th + 1
    print('client thread ', th)
    print('process id '. format)
