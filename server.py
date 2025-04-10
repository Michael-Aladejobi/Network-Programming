import socket 
from _thread import *
import os
import random

th = 0
sa = 0
ca = 0 
da = 0

def stat():
    res = 'Statistical Analysis: '
    res = res + 'Server won with ' + str(sa) + " :client won with " + str(sa)
    return res

def getRandom():
    res = random.randint(1,9)
    return res

def whoWin(s, c):
    global sa, ca, da
    res = ' '
    if c > s:
        res = 'client won with ' + str(c) +' as against server' + str(s)
        ca = ca + 1
        return res
    elif s == c:
        res = res +' Draw: server with' + str(s) + " client with " + str(c)
        da = da + 1
        return res 
    else:
        res = 'server won with ' + str(s) +' as against client' + str(c)
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
            print('game ended!')
            break
        clientNo = int(data)
        serverNo = getRandom()

        log = f'server plays {serverNo}, client plays {clientNo}'
        con.sendall(bytes(log.encode('ascii')))

        whowon = whoWin(serverNo, clientNo)
        print(whowon)
        con.sendall(bytes(whowon.encode('ascii')))


ss = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)
print('server start: ')

host = socket.gethostname()
port = 9999

ss.bind((host, port))
ss.listen(5)

while True:
    con, addr = ss.accept()
    print('Connected to addr {0}, port no. {1}'.format(addr[0], addr[1]))

    start_new_thread(func,(con,))
    th = th + 1
    print('thread no.: ', th)

    print('process ID: '.format(os.getpid()))