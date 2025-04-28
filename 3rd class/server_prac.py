import socket
from _thread import *
import os
import random

th = 0
sa = 0
ca = 0
da = 0

def randonNum():
    x = random.ranint(1, 10)
    return x

def stat():
    global sa, ca, da

    res = 'Statistical Analysis'
    res = 'Server won with ' + str(sa) + " : Client won with " + str(ca) + ' They draw with ' + str(da)
    return res    

def whoWon(s, c):
    global sa, ca, da
    res = ''
    if c > s:
        res = res + 'client won wwith ' + str(c) + ' as against server ' + str(s)
        ca = ca + 1
    elif c == s:
        res = res + 'draw: client with ' + str(c) + ' server with '+ str(s)
        da = da + 1
    else:
        res = res + 'server won with ' + str(s) + ' as against client ' + str(c)
    return res

def func(con):
    data = con.recv(1024)
    print('message from client: ', data)

    msg = input('message to client: ')
    con.sendall(bytes(msg.encode('ascii')))

    data = con.recv(1024)
    while True:
        if not data or data == 'bye':
            print('session ended!')
            break
        clientNo = int(data)
        serverNo = randonNum()

        result = whoWon(serverNo, clientNo)
        print(result)
        con.sendall(bytes(result.encode('ascii')))

        stats = stat()
        print(stats)
        con.sendall(bytes(result.encode('ascii')))

        