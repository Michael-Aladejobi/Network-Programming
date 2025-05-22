import socket
import threading
import os
import random

th = 0 
guess_count = 0
max_guesses = 5

clients = {}

def get_treasure():
    x = random.randint(1, 50)
    return x

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
        res = "Hot (Close)"
        return res
    else:
        res = "Cold (Far)"
        return res
    
def func(addr, data, ss):
    global guess_count
    global max_guesses

    treasure = get_treasure()
    print(f'Treasure hidden at: {treasure}')

    msg = 'Welcome to Hot or Close Treasure hunt Game. \n You only have 5 guesses: '
    msg = str.encode(msg)
    ss.sendto(msg, addr)

    while True:
        con, data = ss.recvfrom(1025)
        print('Message from client b/f decoding: ', con)

        data = con.decode()

        if not data:
            print('Game Ended!')
            break

        if data.lower().strip() == 'bye':
            print('Game Over!')
            break

        client_guess