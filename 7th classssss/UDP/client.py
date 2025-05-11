import socket
import pickle

cs = socket.socket()
print('Client starting...')

host = '127.0.0.1'
port = 7001

cs.connect((host, port))

msg = input('Message to server: ')
cs.send(msg.encode())

data = cs.recv(1024).decode()
print('Server response:', data)

data = cs.recv(1024)
arr = pickle.loads(data)
print('Game array:', arr)

while True:
    index = input('Enter index (0-3) or "bye": ')
    if index == 'bye':
        cs.send(b'bye')
        break
    
    value = input('Enter value (1-9): ')
    
    cs.send(index.encode())
    cs.send(value.encode())
    
    data = cs.recv(1024)
    if data == b'win':
        print('You won!')
        break
    
    arr = pickle.loads(data)
    print('After your move:', arr)
    
    data = cs.recv(1024)
    if data == b'win':
        print('Server won!')
        break
    
    arr = pickle.loads(data)
    print('After server move:', arr)

cs.close()




