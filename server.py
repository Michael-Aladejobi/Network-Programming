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
    res = res + f'server won with {sa}, client won with {ca} !'
    return res

def whoWon(s, c):
    global sa, ca, da
    res = ''
    if c > s:
        res = res + f'client won with {c} as against server with {s}'
        ca = ca + 1
        return res
    elif c == s:
        res = res + f'draw:  client with {c} as against server { s}'
        da = da + 1
        return res
    else:
        res = res + f'server won with {s} as against client {c}'
        sa = sa + 1
        return res
    
def randomNo():
    res = random.randint(1, 9)
    return res

def func(con):
    data = con.recv(1024).decode()
    print('message from client: ', data)

    msg = input( 'message to client: ')
    con.sendall(msg.encode('ascii'))

    while True:
        data = con.recv(1024).decode()
        if not data:
            print('session ended')
        clientNo = int(data)
        serverNo = randomNo()
        msg = 'server No: {0}, client No: {1}'.format(clientNo, serverNo)
        print(msg)
        con.sendall(msg.encode('ascii'))

        res = whoWon(serverNo, clientNo)
        print(res)
        con.sendall(res.encode('ascii'))

        stats = stat()
        print(stats)
        con.sendall(stats.encode('ascii'))


ss = socket.socket(family = socket.AF_INET, type = socket.SOCK_STREAM)
print('server start: ')
host = socket.gethostname()
port = 3000
ss.bind((host, port))
ss.listen(4)
while True:
    con, addr = ss.accept()
    print('address client {0} and port no {1}'.format(addr[0], addr[1]))
    start_new_thread(func, (con,))
    th = th + 1
    print('thread no {0} and process id {1}'.format(th, os.getpid()))