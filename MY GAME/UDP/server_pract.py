import socket
import threading
import os
import random

th = 0
guess_count = 0
max_guesses = 5

clients = {}

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
        treasure = treasure + random.choice([-1,1])
        return treasure
    
def hot_or_cold(treasure, guess):
    distance = abs(treasure - guess)
    if distance <= 5:
        msg = "Hot(CLose)"
        return msg
    else:
        msg = "Cold(Far)"
        return msg
    
def func(addr, data, ss):
    global guess_count
    global max_guesses

    if addr not in clients:
        treasure = get_treasure()
        clients[addr] = {"treasure":treasure, "guess_count":0}
        msg = 'Welcome to Hot or Cold Treasure Hunt!\n You have jusdt 5 guesses.'
        msg = msg.encode(msg)
        ss.sendto(msg, addr)
        return
    
    while True:
        data, addr = ss.recvfrom(1024)
        data = data.decode()

        if not data:
            print('Game ended')
            break
        if data.lower().strip() == 'bye':
            print('Game Ended')
        
        print('message from clien: ', data)
        guess_count = guess_count + 1
        try:
            client_guess = int(data)
            if client_guess < 1 or client_guess > 50:
                msg = 'Outta bound. Enter 1 - 50: '
                print(msg)
                ss.sendto(msg.encode(), addr)
                continue
        except ValueError:
            msg = 'Enter valid value'
            print(msg)
            ss.sendto(msg.encode(), addr)

        
                