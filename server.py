import socket
from _thread import *
import os
import random

th = 0
sa = 0
ca = 0
da = 0

def stat():
    res = 'statistical result: '
    res = res + ' server win with ' + str(sa) + " client wins with " + str(ca) + ' game draw with ' + str(da)
    return res

def whoWon(s, c):
    res = ' '
    if s > c:
        res = res + 'server won with ' + str(s) + ' as against client ' + str(c)
        sa = sa + 1
    elif s == c:
        res = res + " draw: " + 'server with ' + str(s) + " cleint with " + str(c)
        da = da + 1
    else:
        res = res + ' client won with ' + str(c) + ' as against server ' + str(s)
        ca = ca + 1
    return res

def getRandom():
    res = random.randint(1, 9)
    return res

def func(con):
    data = con.recv(1024).decode()
    print('message to client: ', data)
    