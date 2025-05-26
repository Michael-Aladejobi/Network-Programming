import socket
from _thread import *
import os
import random

th = 0
guess_count = 0
max_guesses = 0

def get_treasure():
    treasure = random.randint(1, 50)
    return treasure

def move_treasure(treasure):
    if treasure == 1:
        treasure = treasure + 1
        return treasure
    elif treasure == 50:
        treasure = treasure - 1
        return treasure
    else:
        treasure = treasure + random.choice([-1, 1])
        return treasure

def hot_or_cold(treasure, guess):
    distance = abs(treasure - guess)

    if distance <= 5:
        msg = "Hot (Close)"
        return msg
    else:
        msg = "Cold ( Close)"
        return msg

def func:
    pass

ss = socket.socket(family=socket.AF_INET, type = socket.SOCK_STREAM)
print('Server start: ')

host = socket.gethostname()
port = 6000