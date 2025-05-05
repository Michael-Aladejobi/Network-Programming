import socket
import random
from _thread import *
import os

th = 0
ca = 0
sa = 0
da = 0

def getRandom():
    x = random.randint(1, 10)
    return x

def stats():
    global sa, ca, da
    res = "statistical analysis: "
    res = res + f"server won with {sa}, cliant won with {ca}, the draw with {da} "
    return res

def whoWon(s, c):
    global sa, ca, da
    res = ' '
    if c > s:
        res = f' client won with {c} as against server with {s}'
        ca = ca + 1
    elif c == s:
        res = f' Draw: server with {s}, client with {c}'
        da = da + 1
    else:
        res = f' server won with {s}, as against client with {c}'
        sa = sa + 1
    return res

def func(addr):
    global ss
    while True:
        con, addr = ss.recvfrom(1024)
        data = con.decode()
        if not data:
            print('game ended')
            break
        if data.lower().strip() == 'bye':
            print('game ended')
            break
        print('message from client to send (1 - 10): ', data)

        clientNum = int(data)
        serverNum = getRandom()

        res = whoWon(serverNum, clientNum)
        print(res)
        ss.sendto(res, (addr))

        stat = stats()
        ss.sendto(stat, (addr))

ss = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
print('server start: ')

host = socket.gethostname()
port = 6000
ss.bind((host, port))

while True:
    con, addr = ss.recvfrom(1024)
    print('Connected to {}'.format(addr))

    data = con.decode()
    print('message from client: ', data)

    msg = input('message to client: ')
    msg = str.encode(msg)
    ss.sendto(msg, (addr))

    start_new_thread(func, (addr,))
    th = th + 1
    print('thread no: ', th)

    print('process id: {}'.format(os.getpid()))