# Server_client Thread using TCP

import socket 
from _thread import *
import os

th = 0 #counter var

def func(c):
    data = c.recv(1024).decode()
    print('message from client : ', data)
    
ss = socket.socket(family=socket.AF_INET, type = socket.SOCK_STREAM)
print("Start Server: ")

host = socket.gethostname()
port = 9500 

ss.bind((host , port))
ss.listen(5)

while True:
    con, addr = ss.accept()
    print("address client conn. {} and port no. {}".format (addr[0], addr[1]))
    start_new_thread(func, (con,))

    th = th + 1
    print('client thread ', th)
    print('process id {}'. format(os.getpid())) #get process id