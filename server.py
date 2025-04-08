import socket
from _thread import *
import os
import random

th = 0
sa = 0
ca = 0
da = 0

def stat():
    res = "Statistical analysis: "
    res = res + " server won with " + str(sa) + ": client won with " + str(ca)
    return res

def random():
    res = random.randint()
    return res

def whoWon(s, c):
    global sa, ca, da
    res = ' '
    if c > s:
        res = res + 'client won with ' + str(c) + ' as against server with' + str(s) 
        ca = ca + 1
    elif c == s:
         res = res + 'draw: client ' + str(c) + ' as against server' + str(s)
         da = da + 1
    else:
         res = res + 'server won with ' + str(s) + ' as against client with' + str(c) 
         sa = sa + 1

def func():
    
