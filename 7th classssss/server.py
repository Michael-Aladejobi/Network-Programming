import socket
import random
import pickle

arr = []

N = 4
M = 9

def genArray():
   
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
    if ((index) < 0 or (index > N)):
        print('Index Error')
        return False
    if ((value > arr[index]) or (value < 0)):
        print('Impossible to subtract less value')
        return False #[4,3,2,1] - [5, 2 2 1] = error
    else:
        arr[index] = arr[index] - value
        return True

def isWinner(arr):
    return all(x == 0 for x in arr)

ss = socket.socket()
print('server start: ')

host = '127.0.0.1'
port = 7001

ss.bind((host, port))
ss.listen(5)
con, addr = ss.accept()

print(f'Address client {addr[0]} abd port no.: {addr[1]}')

data = con.recv(1024)
print('message without decoding: ', data)
data = data.decode()
print('message after decoding: ', data)

msg = input('send index and corresponding value: ')
con.sendall(bytes(msg.encode('ascii')))

genArray()
print('Array Game: ', arr)
data_array = pickle.dumps(arr)
con.send(data_array)

while True:

    data = con.recv(1024).decode()
    if data.lower().strip() == 'bye':
        print('game over')
        break
    
    indexCli = int(data)

    data = con.recv(1024).decode()
    valueCli = int(data)

    indexSer = genIndex()
    valueSer = genValue()

    print(f'Client index {indexCli} and value {valueCli}')
    print(f'Server index {indexSer} and value {valueSer}')

    if pop(arr, N, indexCli, valueCli):
        print('array game after client deduction: ', arr)
        data_array = pickle.dumps(arr)
        con.send(data_array)
    else:
        con.send(pickle.dumps(arr))


    # who is the winner
    if isWinner(arr):
        con.send(b'win')
        print('client has won')
        break




    if pop(arr, N, indexSer, valueSer):
        print('array game after client deduction: ', arr)
        data_array = pickle.dumps(arr)
        con.send(data_array)
    else:
        con.send(pickle.dumps(arr))


    # who is the winner\---->
    if isWinner(arr):
        con.send(b'win')
        print('server has won')
        break