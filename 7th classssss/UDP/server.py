import socket
import random
import pickle
import threading

arr = []
N = 4
M = 9

def genArray():
    global arr
    arr = []
    for i in range(N):
        x = random.randint(1, M)
        arr.append(x)

def genIndex():
    x = random.randint(0, N-1)
    return x

def genValue():
    x = random.randint(1, M)
    return x

def pop(arr, N, index, value):
    if index < 0 or index >= N:
        print('Index Error')
        return False
    if value > arr[index] or value < 0:
        print('Impossible to subtract less value')
        return False
    else:
        arr[index] -= value
        return True

def isWinner(arr):
    return all(x == 0 for x in arr)

def handle_client(con, addr):
    print(f'Client connected: {addr}')
    
    # Initial message
    data = con.recv(1024)
    print('Client message:', data.decode())
    
    con.send(b'Game started')
    
    # Generate and send array
    genArray()
    print('Game array:', arr)
    con.send(pickle.dumps(arr))
    
    while True:
        # Client move
        indexCli = int(con.recv(1024).decode())
        valueCli = int(con.recv(1024).decode())
        
        # Server move
        indexSer = genIndex()
        valueSer = genValue()
        
        print(f'Client move: index {indexCli}, value {valueCli}')
        print(f'Server move: index {indexSer}, value {valueSer}')
        
        # Process client move
        if pop(arr, N, indexCli, valueCli):
            print('After client move:', arr)
            con.send(pickle.dumps(arr))
        else:
            con.send(pickle.dumps(arr))
            continue
        
        # Check winner
        if isWinner(arr):
            con.send(b'win')
            print('Client won')
            break
        
        # Process server move
        if pop(arr, N, indexSer, valueSer):
            print('After server move:', arr)
            con.send(pickle.dumps(arr))
        else:
            con.send(pickle.dumps(arr))
            continue
        
        # Check winner
        if isWinner(arr):
            con.send(b'win')
            print('Server won')
            break
    
    con.close()

# Main server code
ss = socket.socket()
print('Server starting...')

host = '127.0.0.1'
port = 7001

ss.bind((host, port))
ss.listen(5)
print(f'Server listening on {host}:{port}')

while True:
    con, addr = ss.accept()
    print(f'New connection from {addr}')
    thread = threading.Thread(target=handle_client, args=(con, addr))
    thread.start()




