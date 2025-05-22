import socket
import threading
import os
import random

th = 0
guess_count = 0
max_guesses = 5

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
    
    print(f"Treasure hidden at: {treasure}")
    msg = "Welcome to the Hot or Cold Treasure Hunt!\nYou have 5 guesses to find the treasure (1-50):"
    msg = str.encode(msg)
    ss.sendto(msg.encode(), addr)


    while True:
        data = con.recv(1024).decode()

        if not data:
            print("Game ended!")
            break

        if data.lower().strip() == 'bye':
            print('Game ended!')
            break

        try:
            client_guess = int(data)

            if client_guess < 1 or client_guess > 50:
                msg = "Invalid guess! Please guess a number between 1 and 50."
                con.sendall(bytes(msg.encode('ascii')))
                continue

        except ValueError:
            msg = "Invalid input! Please enter a valid number."
            con.sendall(bytes(msg.encode('ascii')))
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

   

    

ss =socket.socket(socket.AF_INET, socket.SOCJ_DGRAM)
print('Server start: ')

host = socket.gethostname()
port = 6000

ss.bind((host, port))
print(f"Connected to {host}, port: {port}")

while True:
    con, addr = ss.recvfrom(1024)
    print('message from client b/f decoding: ', con)
    data = con.decode()
    print("message from client after decoding: ", data)

    thread_start = threading.Thread(target=func, args=(addr, data, ss))
    thread_start.start()

    th = th + 1
    print("Thread no: ", th)

    print("Process ID: ", os.getpid())