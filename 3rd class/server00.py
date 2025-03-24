import socket
from _thread import *
import os
import random

th = 0 #Thread counter var

def whoWon(s, c):
    r = ''
    if c > s:
        r = r + ' client won with' + str(c) + ' as against server with ' + str(s)
    elif c == s:
        r = r + ' draw : client with ' + str(c) + ' equal sever no with ' + str(s)
    else:
          r = r + ' server won with' + str(s) + ' as against client with ' + str(c)


def genRandom():
    x = random.randint(1, 9)
    return x


def fun(ss2):
    data = ss2.recv(1024).decode()
    print('Message from client: ', data)

    msg = input('Message to client: ')
    ss2.sendall(bytes(msg.encode('ascii')))

    data = ss2.recv(1024).decode()
    print('Message from client: ', data)
    clientNo = int(data)

    #Generate randome number
    re = genRandom()
    serverNo = re
    print('Server no {} and client no {}'.format(serverNo, clientNo ))

    rr = whoWon(serverNo, clientNo)

ss = socket.socket(family = socket.AF_INET, type = socket.SOCK_STREAM)

print('Server Start: ')
host = socket.gethostname()
port = 6000

ss.bind((host, port))
ss.listen(4)

while True:
    ss2, addr = ss.accept()
    print('Address client {0} and port no. {1}'.format(addr[0], addr[1]))
    start_new_thread(fun, (ss2,))

    th = th + 1 #client counter
    #nxt, print with process identification
    print('Thread no. {0} and process ID {1}'.format(th, os.getpid()))