import socket 
from _thread import *
import os
import random

th = 0
sa = 0
ca = 0 
da = 0

def stat():
    res = 'Statistical Analysis: '
    res = res + 'Server won with ' + str(sa) + " :client won with " + str(sa)
    return res

def getRandom():
    res = random.randint(1,9)
    return res

def whoWin(s, c):
    global sa, ca, da
    res = ' '
    if c > s:
        res = 'client won with ' + str(c) +' as against server' + str(s)
        ca = ca + 1
        return res
    elif s == c:
        res = res +' Draw: server with' + str(s) + " client with " + str(c)
        return res