import socket
import pickle


arr = []

def genArray(arr):
    num = input('enter array length---->: ')
    num = int(num)

    for i in range(num):
        k = input('array value %i: ' %i)
        k = int(k)
        arr.append(k)


cs = socket.socket(family=socket.AF_INET, type = socket.SOCK_STREAM)
print('client server: ')

host = socket.gethostname()
port = 7000

cs.connect((host, port))

msg = input('message to server: ')
cs.send(bytes(msg.encode('ascii')))

data = cs.recv(1024).decode()
print('message from server: ', data)

genArray(arr)
print(arr)
data_arr = pickle.dumps(arr)
cs.send(data_arr)

data = cs.recv(1024).decode()
print('add, avg, variation and standard dev from server: ', data)