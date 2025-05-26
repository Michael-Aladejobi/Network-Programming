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

def func(con):
    global guess_count 
    global max_guesses

    treasure = get_treasure()

    msg = "Welcome to Hot or Close Treasure Hunt. You only have 5 guesses. Good Luck!"
    con.sendall(bytes(msg.encode('ascii')))

    while True:
        data = con.recv(1024)
        data = data.decode()

        if not data:
            print("Game over")
            break
        if data.lower().strip() == 'bye':
            print("Game Over")
            break

        print('message from client :', data)

        guess_count = guess_count + 1

        try:
            client_guess = int(data)
            if client_guess < 1 or client_guess > 50:
                msg = "Out of range. Enter btw 1 and 50"
                print("Client side: ", msg)
                con.sendall(bytes(msg.encode('ascii')))
                continue
        except ValueError:
            msg = "Invalid Valid. Enter a valid value."
            print('Client side: ', msg)
            con.sendall(bytes(msg.encode('ascii')))
        
        if client_guess == treasure:
            msg = "Congratulations! Client found the treasure."
            print(msg)
            con.sendall(bytes(msg.encode('ascii')))
            break
        elif client_guess >= guess_count:
            msg = "Out of Guess. Server Won!"
            print(msg)
            con.sendall(bytes(msg.encode('ascii')))
            break
        else:
            remaining_guesses = max_guesses - guess_count
            result = hot_or_cold(treasure, client_guess)
            result = result + f""
            print(result)
            con.sendall(bytes(result.encode('ascii')))

            move_treasure(treasure)

    



ss = socket.socket(family=socket.AF_INET, type = socket.SOCK_STREAM)
print('Server start: ')

host = socket.gethostname()
port = 6000

ss.bind((host, port))
ss.listen(5)

while True:
    con, addr = ss.accept()
    print("Connected to addr {0}, port {1}".format(addr[0], addr[1]))

    start_new_thread(func, (con,))

    th = th + 1
    print("Thread no.: ", th)

    print("Process ID: ", os.getpid())