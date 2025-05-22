import socket
from _thread import *
import os
import random

th = 0
ca = 0
sa = 0
da = 0

def stat():
    res = 'statistical analysis: '
    res = res + f' Server won with {sa}, Client won with {ca}, Draw with {da}'
    return res

def genRandom():
    x = random.ranint(1, 9)
    return x

def whoWon(c, s):
    global sa, ca, da
    if c > s:
        res = f'Client won with {c} as against server {s}'
        ca = ca + 1
    elif c == s:
        res = f'Draw: Server {s}, Client {c}'
        da = da + 1
    else:
        res = f'Derver won with {s} as against client {c}'
        sa = sa + 1
    return res