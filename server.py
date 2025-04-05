import socket
from _thread import *
import os
import random

th = 0
sa = 0
ca = 0
da = 0

def stat():
    res = "statistical analysis:  "
    res = res + ' server won with ' + str(sa) + ' client won with '+ str(ca)
    return res

def whoWon(s, c):
    res = " "
    if s > c:
        res = 'server won with ' + str(s) +' as against client with ' + str(c)
        sa = sa + 1
    elif s == c:
        res = ' draw: ' + ' server score ' + str(s) + ' client score ' + str(c)
        da = da + 1
    else:
        res = 'client won with ' + str(c) +' as against server with ' + str(s)
    return res

def getRandom():
    res = random.randint(1, 9)
    return res

def func(con):
    data = con.recv(1024).decode()
    print('message from client: ', data)