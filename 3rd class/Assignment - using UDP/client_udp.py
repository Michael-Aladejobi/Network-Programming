import socket
import threading
import os
import random


th = 0
sa = 0
ca = 0
da = 0


def genRandom():
    return random.randint(1, 9)


def whoWon(s, c):
    global sa, ca, da
    if c > s:
        ca += 1
        return f"Client won , with {c} vs Server {s}"
    elif c == s:
        da += 1
        return f"Draw: Client {c} = Server {s}"
    else:
        sa += 1
        return f"Server won with {s} vs Client {c}"


def stat():
    return f"Statistical analysis: Server won: {sa}, Client won: {ca}, Draws: {da}"

def handle_client(data, addr, server_socket):
    try:
        client_num = int(data)
        server_num = genRandom()
        print(f"[{addr}] Server No: {server_num}, Client No: {client_num}")

        result = whoWon(server_num, client_num)
        server_socket.sendto(result.encode(), addr)
        server_socket.sendto(stat().encode(), addr)

    except ValueError:
        server_socket.sendto("Invalid input. Please send a number.".encode(), addr)


ss = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
host = "127.0.0.1"
port = 3000
ss.bind((host, port))

print("UDP Server started...")

while True:
    data, addr = ss.recvfrom(1024)
    message = data.decode().strip()

    if message.lower() == "bye":
        print(f"[{addr}] ended session.")
        ss.sendto("Session ended. Bye!".encode(), addr)
        continue

    print(f"[{addr}] Message from client: {message}")
    thread = threading.Thread(target=handle_client, args=(message, addr, ss))
    thread.start()
    
    th += 1
    print(f"Active threads: {th} | Process ID: {os.getpid()}")
