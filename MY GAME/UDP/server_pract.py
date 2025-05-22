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

    if addr not in clients:
        treasure = get_treasure()
        clients[addr] = {"Treasure":treasure, "guess_count": 0}
        print(f'Treasure hidden at: {treasure}')

        msg = 'Welcome to Hot or Close Treasure hunt Game. \n You only have 5 guesses: '
        msg = str.encode(msg)
        ss.sendto(msg, addr)
        return

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

        try:
            client_guess = int(data)

            if client_guess < 1 or client_guess > 50:
                msg = 'Value out of bound! Enter 1 - 50: '
                msg = str.encode(msg)
                ss.sendto(msg, addr)
                return
        except ValueError:
            msg = "Invalid Value: Please enter  1 - 50: "

        guess_count = guess_count  + 1
        clients[addr]["guess_count"] = guess_count

        if client_guess == treasure:
            msg = f"Congratulations! You found the reasure in {guess_count} guesses."
            msg = str.encode(msg)
            ss.sendto(msg, addr)
            del clients[addr]
        elif guess_count >= max_guesses:
            msg = 'Server won, Client ran out of guesses!'
            print(msg)
            ss.sendto(msg, addr)
            del clients[addr]
            return
        else:
            remaining_guess = max_guesses - guess_count
            result = hot_or_cold(treasure, client_guess)
            msg =  f"{result} \n {remaining_guess}"
            ss.sendto(msg.encode(), addr)

            