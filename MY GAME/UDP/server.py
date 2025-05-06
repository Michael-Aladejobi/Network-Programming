import socket
import threading
import os
import random

th = 0
clients = {}

def get_treasure():
    return random.randint(1, 50)

def move_treasure(treasure):
    if treasure == 1:
        return treasure + 1
    elif treasure == 50:
        return treasure - 1
    else:
        return treasure + random.choice([-1, 1])

def hot_or_cold(treasure, guess):
    distance = abs(treasure - guess)
    if distance <= 5:
        return "Hot (close)"
    else:
        return "Cold (far)"

def func(addr, message):
    global th

    if addr not in clients:
        treasure = get_treasure()
        clients[addr] = {"treasure": treasure, "guess_count": 0}
        print(f"Treasure hidden at: {treasure} for {addr}")
        ss.sendto(b"Welcome to the Hot or Cold Treasure Hunt!\nYou have 5 guesses to find the treasure (1-50):", addr)
        return

    try:
        guess = int(message)
        if guess < 1 or guess > 50:
            ss.sendto(b"Invalid guess! Please guess a number between 1 and 50.", addr)
            return
    except:
        ss.sendto(b"Invalid input! Please enter a number.", addr)
        return

    clients[addr]["guess_count"] += 1
    treasure = clients[addr]["treasure"]
    guess_count = clients[addr]["guess_count"]
    max_guesses = 5

    if guess == treasure:
        ss.sendto(bytes(f"Congratulations! You found the treasure in {guess_count} guesses!\n".encode()), addr)
        print(f"{addr} found the treasure!")
        del clients[addr]
    elif guess_count >= max_guesses:
        ss.sendto(bytes(f"Game over! Server wins. The treasure was at {treasure}\n".encode()), addr)
        print(f"Server wins - {addr} ran out of guesses.")
        del clients[addr]
    else:
        response = hot_or_cold(treasure, guess)
        remaining = max_guesses - guess_count

        response += f"Guesses remaining: {remaining}"
        ss.sendto(response.encode(), addr)

        treasure = move_treasure(treasure)
        clients[addr]["treasure"] = treasure
        print(f"Treasure moved to: {treasure} for {addr}")

ss = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
print("Server start: ")

host = socket.gethostname()
port = 9999

ss.bind((host, port))
print("Connected to host", host, ", port:", port)

while True:
    data, addr = ss.recvfrom(1024)
    msg = data.decode().strip()
    print(f"Message from client: {msg}")

    threading.Thread(target=func, args=(addr, msg)).start()
    th += 1
    
    print("Thread no.:", th)
    print("Process ID:", os.getpid())
