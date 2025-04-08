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

def whoWon():
    