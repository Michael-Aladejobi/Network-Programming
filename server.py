import socket
from _thread import *
import os
import random

th = 0
sa = 0
ca = 0
da = 0

def getRandom():
    res = random.randint(1,10)
    return res

def stat():
    global sa, ca, da
    res = ""
    res = res + 'server won with ' + str(sa) + " client won with " + str(ca) + ': draw with ' + str(da)
    return res

def whoWon(s, c):
    global sa, ca, da
    res = ''
    if c > s:
        res = res + 'cleint won with' + str(c) +' as agaist server with ' + str(s) 
        ca = ca + 1 
    elif c == s:
        res = res + ' Draw: client with ' + str(c) +' server with ' + str(s)
        da = da + 1
    else:
        res = res + 'server won with' + str(s) +' as agaist client with ' + str(c)
    return res

def func(con):
    data = con.recv(1024).decode() 
    print('message from client: ', data)

    msg = input('message to client: ')
    con.sendall(bytes(msg.encode('ascii')))

    while True:
        data = con.recv(1024).decode()
        if not data:
            print('game ended')
            break
        clientNo = int(data)
        serverNo = getRandom()

        res = whoWon(clientNo, serverNo)
        print(res)
        con.sendall(bytes(res.encode()))

        stats = stat()
        print(stats)
        con.sendall(bytes(stats.encode()))

ss = socket.socket(family = socket.AF_INET, type = socket.SOCK_STREAM)

print('Server Start: ')

host = socket.gethostname()
port = 9999

ss.bind((host, port))
ss.listen(5)

while True:
    con, addr = ss.accept()
    print('Connected to addr {0}, port no. {1}'.format(addr[0], addr[1]))

    start_new_thread(func, (con,))
    th = th + 1
    print('thread no: ', th)

    print('process id:'.format(os.getpid()) )

ss.close()