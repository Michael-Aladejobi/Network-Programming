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
        return treasure + 1
    elif treasure == 50:
        return treasure - 1
    else:
        return treasure + random.choice([-1, 1])


def hot_or_cold(treasure, guess):
    distance = abs(treasure - guess)
    if distance <= 5:
        res = "Hot (close)"
        return res
    else:
        res = "Cold (far)"
        return res


def func(addr, data, ss):
    global guess_count

    if addr not in clients:
        treasure = get_treasure()
        clients[addr] = {"treasure": treasure, "guess_count": 0}
        print(f"Treasure hidden at: {treasure}")
        msg = "Welcome to the Hot or Cold Treasure Hunt!\nYou have 5 guesses to find the treasure (1-50):"
        ss.sendto(msg.encode(), addr)
        return  # Exit for now, wait for next message to continue

    treasure = clients[addr]["treasure"]
    guess_count = clients[addr]["guess_count"]

    if data.lower().strip() == 'bye':
        print(f'[{addr}] Game ended by client.')
        del clients[addr]
        return

    try:
        client_guess = int(data)

        if client_guess < 1 or client_guess > 50:
            msg = "Invalid guess! Please guess a number between 1 and 50."
            ss.sendto(msg.encode(), addr)
            return

    except ValueError:
        msg = "Invalid input! Please enter a valid number."
        ss.sendto(msg.encode(), addr)
        return

    # Update guess count
    guess_count = guess_count + 1
    clients[addr]["guess_count"] = guess_count

    if client_guess == treasure:
        msg = f"Congratulations! You found the treasure in {guess_count} guesses!"
        ss.sendto(msg.encode(), addr)
        print(f"[{addr}] Client found the treasure!")
        del clients[addr]
        return

    elif guess_count >= max_guesses:
        msg = f"Game over! Server wins. The treasure was at {treasure}"
        ss.sendto(msg.encode(), addr)
        print(f"[{addr}] Server won - client ran out of guesses")
        del clients[addr]
        return

    else:
        
        remaining_guess = max_guesses - guess_count
        result = hot_or_cold(treasure, client_guess)
        msg = f"{result}\nGuesses remaining: {remaining_guess}"
        ss.sendto(msg.encode(), addr)

        # Move treasure
        new_pos = move_treasure(treasure)
        clients[addr]["treasure"] = new_pos
        print(f"[{addr}] Treasure moved to: {new_pos}")



ss = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
print("Server start: ")

host = socket.gethostname()
port = 9999

ss.bind((host, port))
print("Connected to host", host, ", port:", port)

while True:
    con, addr = ss.recvfrom(1024)
    data = con.decode().strip()
    print(f"Message from client: {data}")

    threading.Thread(target=func, args=(addr, data, ss)).start()
    
    th = th + 1
    print("Thread no.:", th)

    print("Process ID:", os.getpid())







# Older func(), working but haviing distinct client issue. Seeing old client as a new client everytime

    # def func(addr, data):
    # global th
    # global ss
    # global guess_count

    # if addr not in clients:
    #     treasure = get_treasure()

    #     print(f"Treasure hidden at: {treasure}")
    #     msg = "Welcome to the Hot or Cold Treasure Hunt!\nYou have 5 guesses to find the treasure (1-50):"
    #     msg = str.encode(msg)
    #     ss.sendto(msg, (addr))   
        
    
    # while True:
    #     con, addr = ss.recvfrom(1024)

    #     data = con.decode()
    #     if not data:
    #         print("Game ended!")
    #         break

    #     if data.lower().strip() == 'bye':
    #         print('Game ended!')
    #         break

    #     try:
    #         client_guess = int(data)

    #         if client_guess < 1 or client_guess > 50:
    #             msg = "Invalid guess! Please guess a number between 1 and 50."
    #             msg = str.encode(msg)
    #             ss.sendto(msg, (addr))
    #             continue

    #     except ValueError:
    #         msg = "Invalid input! Please enter a valid number."
    #         msg = str.encode(msg)
    #         ss.sendto(msg, (addr))
    #         continue

    #     guess_count = guess_count + 1
    #     result = hot_or_cold(treasure, client_guess)
        
    #     if client_guess == treasure:
    #         msg = f"Congratulations! You found the treasure in {guess_count} guesses!"
    #         msg = str.encode(msg)
    #         ss.sendto(msg, (addr))
    #         print("Client found the treasure!")
    #         break

    #     elif guess_count >= max_guesses:
    #         msg = f"Game over! Server wins. The treasure was at {treasure}\n"
    #         msg = str.encode(msg)
    #         ss.sendto(msg, (addr))
    #         print("Server won - client ran out of guesses")
    #         break
        
    #     else:
    #         remaining_guess = max_guesses - guess_count

    #         result = result + f"\nGuesses remaining: {remaining_guess}"
    #         result = str.encode(result)
    #         ss.sendto(msg, (addr))            

    #         treasure = move_treasure(treasure)
    #         print(f"Treasure moved to: {treasure}")