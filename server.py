import socket
import calendar
from _thread import *
import os

th = 0

def weekDay(yy, mm, dd):
    res = 'Weekday of date '
    weekday = ['Monday', 'Tuesday', 'Wednesday','Thursday','Friday','Saturday', 'Sunday']

    x = calendar.weekday(yy, mm, dd)
    y = weekday[x]

    res = res + 'year: ' + str(yy) + ' month: ' + str(mm) + ' day: ' + str(dd) + ' is '  + str(y)

    return res

def func(ss):
    con, addr = ss.recvfrom(1023)
    print('Connected to addr: {0}'.format(addr))
    data = con.decode()
    print('message from client: ', data)

    msg = input('message to client(y,m,d): ')
    msg = str.encode(msg)
    ss.sendto(msg, (addr))

    while True:
        con, data = ss.recvfrom(1024)
        data = con.decode()
        if not data:
            print('session ended')
            break
        if data.lower().strip() == 'bye':
            print('session ended by client')
            break
        print('message from client: ', data)

        data = data.split(',')
        yy = int(data[0])
        mm = int(data[1])
        dd = int(data[2])

        res = weekDay(yy, mm, dd)


        msg = res
        msg = str.encode(msg)
        ss.sendto(msg, (addr))

ss = socket.socket(family=socket.AF_INET,type=socket.SOCK_DGRAM)
print('server start: ')

host = socket.gethostname()
port = 9999
ss.bind((host, port))

while True:
    th = th + 1
    print('Thread no: ', th)
    func(ss)