import socket
import calendar
import threading
import os

th = 0

def weekday(y, m, d):
    res = "Weekday of birthday: "
    weekday = ["Mon", "Tue", "Wed", "Thur", "Fri", "Sat", "Sun"]
    x = calendar.weekday(y, m, d)
    re = weekday[x]
    res = res + f" year {y}, month {m}, day{d} is {re}"
    return res

def func(addr, data, ss):
    msg = input('message to server: ')
    msg = str.encode(msg)
    ss.sendto(msg, addr)

    while True:
        con, addr = ss.recvfrom(1024)
        data = con.decode()

        if not data:
            print('Session ended')
            break
        if data.lower().strip() == ' bye':
            print('Session ended!')
            break
        print('message from client: ', data)
        data = data.split(",")
        yr = data[0]
        mm = data[1]
        dd = data[2]

        res = weekday(yr, mm, dd)
        print(res)
        res = str.encode(res)
        ss.sendto(res, addr)

ss = socket.socket(family=socket.AF_INET, type = socket.SOCK_DGRAM)
print('Server start: ')

host = '127.0.0.1'
port = 6000

ss.bind((host, port))

while True:
    con, addr = ss.recvfrom(1024)
    data = con.decode()
    print('message from client: ', data)

    threading.Thread(target = func, args=(addr, data, ss)).start()

    th = th + 1
    print("Thread no: ", th)

    print("Process ID: ".format(os.getpid()))