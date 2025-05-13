import socket
import random
import pickle
import threading


array = []
N = 4
M = 9


def genArray():
    
    for i in range(N):
        x = random.randint(1, M)
        array.append(x)


def genIndex():
    x = random.randint(0, N-1)
    return x


def genValue():
    x = random.randint(1, M)
    return x


def pop(array, N, index, value):
    if ((index) < 0 or (index > N)):
        print('Index Error')
        return False
    if ((value > array[index]) or (value < 0)):
        print('Impossible to subtract less value')
        return False #[4,3,2,1] - [5, 2 2 1] == error
    else:
        array[index] = array[index] - value
        return True


def isWinner(arr):
    return all(x == 0 for x in arr)


def func(con, addr, server_socket):

    global array

    if con.lower().strip() == "hello":

         # Send game array
        server_socket.sendto(pickle.dumps(array), addr) 
        return

    # Ensure received data is numeric before processing
    if not con.isdigit():
        print(f"Invalid input from {addr}: {con}")
        return

    client_index = int(con)
    client_value = server_socket.recvfrom(1024)[0].decode()
    client_value = int(client_value)

    server_index = genIndex()
    server_value = genValue()

    print(f"Client {addr} chose index {client_index} with value {client_value}")
    print(f"Server chose index {server_index} with value {server_value}")

    
    if pop(array, N, client_index, client_value):
        print("Game array after client's move:", array)
        server_socket.sendto(pickle.dumps(array), addr)
    else:
        server_socket.sendto(pickle.dumps(array), addr)

    
    if isWinner(array):
        server_socket.sendto(b"win", addr)
        print("Client wins the game!")
        return

    
    if pop(array, N, server_index, server_value):
        print("Game array after server's move:", array)
        server_socket.sendto(pickle.dumps(array), addr)
    else:
        server_socket.sendto(pickle.dumps(array), addr)

    
    if isWinner(array):
        server_socket.sendto(b"win", addr)
        print("Server wins the game!")


server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_host = "127.0.0.1"
server_port = 7001
server_socket.bind((server_host, server_port))

print("Server Start...")

genArray()
print("Initial game array:", array)

while True:
    con, addr = server_socket.recvfrom(1024)
    threading.Thread(target=func, args=(con.decode(), addr, server_socket)).start()
