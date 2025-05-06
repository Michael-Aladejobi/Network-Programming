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

def client_handler(addr):
    global ss, th
    treasure = get_treasure()
    print(f"Treasure hidden at: {treasure} (Client: {addr})")
    ss.sendto(b"Welcome to the Hot or Cold Treasure Hunt!\nGuess the treasure (1-50):", addr)
    
    while True:
        try:
            data, addr = ss.recvfrom(1024)
            if not data:
                print(f"Client {addr} disconnected")
                break
                
            client_guess = int(data.decode())
            if client_guess < 1 or client_guess > 50:
                ss.sendto(b"Invalid guess! Please guess a number between 1 and 50.", addr)
                continue
                
            response = hot_or_cold(treasure, client_guess)
            ss.sendto(f"Server: {response}\n".encode('ascii'), addr)
            
            if client_guess == treasure:
                ss.sendto(b"Congratulations! You found the treasure!\n", addr)
                print(f"Client {addr} found the treasure!")
                break
                
            treasure = move_treasure(treasure)
            print(f"Treasure moved to: {treasure} (Client: {addr})")
            
        except ValueError:
            ss.sendto(b"Invalid input! Please enter a valid number.", addr)
        except Exception as e:
            print(f"Error with {addr}: {str(e)}")
            break
    
    th = th - 1
    print(f"Client disconnected: {addr}")

ss = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
print("UDP Server started:")

host = socket.gethostname()
port = 9999

ss.bind((host, port))
print(f"Listening on {host}:{port}")

try:
    while True:
        data, addr = ss.recvfrom(1024)
        print(f"New connection from {addr[0]}:{addr[1]}")
        start_new_thread(client_handler, (addr,))
        th = th + 1
        print("Thread no.: ", th)
        print("Process ID: ", os.getpid())
except KeyboardInterrupt:
    print("Server shutting down...")
finally:
    ss.close()