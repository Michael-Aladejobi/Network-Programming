import socket
from _thread import *
import os 
import random

th = 0
sa = 0
ca = 0
da = 0

def randomNum():
    x = random.randint(1, 9)
    return x

def stats():
    global sa, ca, da
    res = "statistical analysis: "
    res = res + f'server won with {sa}, client won with {ca}, game draw is {da}'
    return res

def whoWon(s, c):
    global sa, ca, da
    res = ' '
    if c > s:
        res = res + f" Client won with {c}, as against server with {s}"
        ca = ca + 1
    elif c == s:
        res = res + f" Draw: server with {s}, client with {c}"
        da = da + 1
    else:
        res = res + f" Server won with {s}, as against client with {c}"
        sa = sa + 1
        return res
    
def func(con):
    data = con.recv(1024).decode()
    print('message from client: ', data)

    msg = input('message to client: ')
    con.sendall(bytes(msg.encode('ascii')))

    while True:
        data = con.recv(1024).decode()
        if not data:
            print('Game over')
            break
        if data.lower().strip() == 'bye':
            print('Game over')
            break
        print('message from client: ',data)
        clientNo = int(data)
        serverNo = randomNum()
       

        res = whoWon(serverNo, clientNo)
        print(res)
        con.sendall(bytes(res.encode('ascii')))

        stat = stats()
        print(stat)
        con.sendall(bytes(stat.encode('ascii')))

ss = socket.socket(family=socket.AF_INET, type = socket.SOCK_STREAM)
print('Server start: ')

host = socket.gethostname()
port = 6000

ss.bind((host, port))
ss.listen(5)

while True:
    con, addr = ss.accept()
    print(f'Connected to addr {addr[0]}, port no:{addr[1]}')
    
    start_new_thread(func,(con,))

    th = th + 1
    print('thread no: ', th)

    print(f'proces id: {os.getpid()}')
