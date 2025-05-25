import socket
from _thread import *
import os
import random

th = 0
sa = 0
ca = 0
da = 0

def stat():
    global sa, ca, da
    res = 'statistical analysis: '
    res = res + f" server won with {sa},  : client won with {ca}, Draw: {da}"
    return res

def get_random():
    x = random.randint(1, 9)
    return x

def whoWon(s, c):
    global sa, ca, da
    res = " "
    if c > s:
        res = f'Client won with {str(c)} as against server with {(str(s))}'
        ca = ca + 1
    elif c == s:
        res = f'Draw:  Client with {str(c)} and server with {(str(s))}'
        da = da + 1
    else:
        res = f'Server won with {str(s)} as against client with {(str(c))}'
        sa = sa + 1
    return res

def func(con):
    
    while True:
        data = con.recv(1024).decode()
        if not data:
            msg = 'Game ended'
            print(msg)
            con.sendall(bytes(msg.encode('ascii')))
            break
        if msg.lower().strip() == 'bye':
            msg = 'Game ended'
            print(msg)
            con.sendall(bytes(msg.encode('ascii')))
            break
        print('Message from client: ', data)
        server_guess = get_random()
        client_guess = int(data)

        res = whoWon(server_guess, client_guess)
        print(res)
        con.sendall(bytes(res.encode('ascii')))

        xx = stat()
        con.send(bytes(xx.encode('ascii')))
    
ss = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)
print('Server start: ')

host = '127.0.0.1'
port = 6000

ss.bind((host, port))
ss.listen(5)

while True:
    con, addr = ss.accept()
    print('connected to addr {0}, port {1}'.format(addr[0], addr[1]))

    start_new_thread(func, (con,))
    th = th + 1
    print("Thread no: ", th)

    print("Process ID, ".format(os.getpid()))