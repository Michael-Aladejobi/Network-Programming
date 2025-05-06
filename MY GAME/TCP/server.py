import socket
from _thread import *
import os
import random

th = 0  

def get_treasure():
    res = random.randint(1, 50)
    return res

def move_treasure(treasure):
    if treasure == 1:
        treasure = treasure + 1
    elif treasure == 50:
        treasure = treasure - 1
    else:
        treasure = treasure + random.choice([-1, 1])
    return treasure

def hot_or_cold(treasure, guess):
    distance = abs(treasure - guess)
    if distance <= 5:
        return "Hot (close)"
    else:
        return "Cold (far)"

def func(con):
    treasure = get_treasure()  
    guess_count = 0
    max_guesses = 5
    print(f"Treasure hidden at: {treasure}")
    con.sendall(b"Welcome to the Hot or Cold Treasure Hunt!\nYou have 5 guesses to find the treasure (1-50):")

    while True:
        data = con.recv(1024).decode()
        if not data:
            print("Game ended!")
            break

        try:
            client_guess = int(data)
            if client_guess < 1 or client_guess > 50:
                msg = "Invalid guess! Please guess a number between 1 and 50."
                con.sendall(bytes(msg.encode('ascii')))
                continue

        except ValueError:
            con.sendall(b"Invalid input! Please enter a valid number.")
            continue

        guess_count = guess_count + 1
        response = hot_or_cold(treasure, client_guess)
        
        if client_guess == treasure:
            msg = f"Congratulations! You found the treasure in {guess_count} guesses!"
            con.sendall(bytes(msg.encode('ascii')))
            print("Client found the treasure!")
            break

        elif guess_count >= max_guesses:
            msg = f"Game over! Server wins. The treasure was at {treasure}\n"
            con.sendall(bytes(msg.encode('ascii')))
            print("Server won - client ran out of guesses")
            break
        
        else:
            remaining = max_guesses - guess_count
            response = response + f"\nGuesses remaining: {remaining}"
            con.sendall(bytes(response.encode('ascii')))
            treasure = move_treasure(treasure)
            print(f"Treasure moved to: {treasure}")

    con.close()

ss = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)
print("Server started:")

host = socket.gethostname()
port = 6000

ss.bind((host, port))
ss.listen(5)

while True:
    con, addr = ss.accept()
    print("Connected to addr {0}, port no. {1}".format(addr[0], addr[1]))

    start_new_thread(func, (con,))
    th = th + 1
    print("Thread no.: ", th)
    print("Process ID: ", os.getpid())