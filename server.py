import socket
from _thread import*
import os
import random

th = 0
sa = 0
ca = 0
da = 0
def stat():
    re = 'statistical analysis :  '
    re = re +' server won with '+str(sa)+' client won with '+str(ca)+'  game draw with '+str(da)
    return re


def whoWon(s, c):
    global sa, ca, da
    r = ''
    if c > s:
        r = r +' client won with '+str(c)+' as against server with  '+str(s)
        ca = ca + 1
    elif c == s:
        r = r +' draw : client with '+str(c)+' equal server no with  '+str(s)
        da = da + 1
    else:
        r = r + ' server won with ' + str(s) + ' as against client with  ' + str(c)
        sa = sa + 1
    return r
def genRandom():
    x = random.randint(1, 9)
    return x


def fun(con):
    data = con.recv(1024).decode()
    print('message from client : ',data)

    msg = input('message to client : ')
    con.send(bytes(msg.encode('ascii')))

    while True:

        data = con.recv(1024).decode()
        print('message from client : ', data)
        if not data:
            print('end game ')
            break
        cliNo = int(data)

        re = genRandom()
        serNo = re
        print('server no {0} and client no {1} '.format(serNo,cliNo ))
        rr = whoWon(serNo, cliNo)
        print('message to client ',rr)
        con.send(bytes(rr.encode('ascii')))

        xx = stat()
        con.send(bytes(xx.encode('ascii')))

ss = socket.socket(family = socket.AF_INET, type = socket.SOCK_STREAM)
print('server start: ')
host = socket.gethostname()
port = 9000
ss.bind((host, port))
ss.listen(4)
while True:
    con, addr = ss.accept()
    print('address client {0} and port no {1}'.format(addr[0], addr[1]))
    start_new_thread(fun, (con,))
    th = th + 1
    print('thread no {0} and process id {1}'.format(th, os.getpid()))