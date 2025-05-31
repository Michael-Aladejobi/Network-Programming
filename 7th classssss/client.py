import socket
import pickle

cs = socket.socket()
print('client start: ')

host = '127.0.0.1'
port = 7001

cs.connect((host, port))

msg = input('messagr to server: ' )
cs.send(bytes(msg.encode('ascii')))

data = cs.recv(1024).decode()
print(f'message from server: {data}')

data = cs.recv(1024)
data_array = pickle.loads(data)
print('Array Game: ', data_array)   

# input index-----
indexCli = input('enter index from 0 - 3: ')
while indexCli.strip() != 'bye':
    cs.sendall(bytes(indexCli.encode('ascii')))

    # input___ value
    valueCli = input('enter value from 1 - 9: ')
    cs.sendall(bytes(valueCli.encode('ascii')))

    # client has woon
    data = cs.recv(1024)
    if data == b'win':
        print('client has won')
        break

    data_arr = pickle.loads(data)
    print('array game after client deduction: ', data_arr)


    # server
    data = cs.recv(1024)
    if data == b'win':
        print('server has won')
        break

    data_arr = pickle.loads(data)
    print('array game after server deduction: ', data_arr)


    if all(x==0 for x in data_arr):
        print('clint won and game over')
        break

    indexCli = input('enter index from 0 - 3 or type (bye) to quit: ')

cs.send(b'bye')
cs.close()