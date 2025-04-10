import socket
from _thread import *
import os
import random

th = 0

def get_treasure():
    """Initialize and return the treasure's position."""
    return random.randint(1, 50)

def move_treasure(treasure):
    """Move the treasure slightly."""
    if treasure == 1:
        treasure += 1
    elif treasure == 50:
        treasure -= 1
    else:
        treasure += random.choice([-1, 1])
    return treasure

def hot_or_cold(treasure, guess):
    """Determine if the guess is 'Hot' or 'Cold'."""
    distance = abs(treasure - guess)
    if distance <= 5:
        return "Hot (close)"
    else:
        return "Cold (far)"

def func(con):
    treasure = get_treasure()  # Initialize the treasure
    print(f"Treasure hidden at: {treasure}")
    con.sendall(b"Welcome to the Hot or Cold Treasure Hunt!\nGuess the treasure (1-50):")

    while True:
        data = con.recv(1024).decode()
        if not data:
            print("Game ended!")
            break

        try:
            client_guess = int(data)
            if client_guess < 1 or client_guess > 50:
                con.sendall(b"Invalid guess! Please guess a number between 1 and 50.")
                continue
        except ValueError:
            con.sendall(b"Invalid input! Please enter a valid number.")
            continue

        response = hot_or_cold(treasure, client_guess)
        con.sendall(bytes(f"Server: {response}\n".encode('ascii')))

        if client_guess == treasure:
            con.sendall(b"Congratulations! You found the treasure!\n")
            print("Client found the treasure!")
            break

        treasure = move_treasure(treasure)  # Move the treasure slightly
        print(f"Treasure moved to: {treasure}")

    con.close()

ss = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)
print("Server started:")

host = socket.gethostname()
port = 9999

ss.bind((host, port))
ss.listen(5)

while True:
    con, addr = ss.accept()
    print("Connected to addr {0}, port no. {1}".format(addr[0], addr[1]))

    start_new_thread(func, (con,))
    th = th + 1
    print("Thread no.: ", th)

    print("Process ID: ", os.getpid())