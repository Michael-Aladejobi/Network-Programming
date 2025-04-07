import socket
from _thread import *
import os
import random

th = 0
sa = 0
ca = 0
da = 0

def stat():
    res = 'statistical result: '
    res = res + ' server win with ' + str(sa) + " client wins with " + str(ca) + ' game draw with ' + str(da)
    return res

def whoWon(s, c):
    global sa, ca, da
    res = ' '
    if s > c:
        res = res + 'server won with ' + str(s) + ' as against client ' + str(c)
        sa = sa + 1
    elif s == c:
        res = res + " draw: " + 'server with ' + str(s) + " cleint with " + str(c)
        da = da + 1
    else:
        res = res + ' client won with ' + str(c) + ' as against server ' + str(s)
        ca = ca + 1
    return res

def getRandom():
    res = random.randint(1, 9)
    return res

def func(con):
    data = con.recv(1024).decode()
    print('message to client: ', data)

    msg = input('message to cient: ')
    con.sendall(bytes(msg.encode('ascii')))

    while True:
        data = con.recv(1024).decode()
        if not data:
            print('game ended!')
            break
        clientNo = int(data)
        serverNo = getRandom()
        print('server no: {0}, client: {1}'.format(serverNo, clientNo))

        res = whoWon(clientNo, serverNo)
        print("message to client: ", res)
        con.sendall(bytes(res.encode('ascii')))

        stats = stat()
        print(stats)
        con.sendall(bytes(stats.encode('ascii')))


ss= socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)

print('server start: ')

host = socket.gethostname()
port = 6000

ss.bind((host, port))
ss.listen(5)

while True:
    con, addr = ss.accept()
    print('Connected to addr {0}, port no. {1}'.format(addr[0], addr[1]))
    start_new_thread(func, (con,))
    th = th + 1
    print('thread no: ', th)

    print('process id: '.format(os.getpid()))