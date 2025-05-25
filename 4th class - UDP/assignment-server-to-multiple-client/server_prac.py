import socket
import threading
import os
import calendar

th = 0

def weekday(y, m, d):
    res = 'Birthday of weekday of: '
    wkd = ['mon', 'tue','wed','thur','fri','sat','sun']
    wkd_index = calendar.weekday(y, m, d)
    wkd_index_value = wkd[wkd_index]
    res = res + f'year {str(y)}, month {str(m)}, day {str(d)}'
    
    return wkd_index_value

def func(addr, data, ss):
    con, addr = ss.recvfrom(1024)
    print('message from client: ',con.decode())

    msg = input('message to client: ')
    msg = str.encode(msg)
    ss.sendto(msg, addr)

    while True:
        con, addr = ss.recvfrom(1024)
        data = con.decode()

        if not data or data.lower().strip() == 'bye':
            print('Game ended')
            break

        print('message from client: ', data)

        data = data.split(",")
        yy = data[0]
        mm = data[1]
        dd = data[2]

        wkd = weekday(yy, mm, dd)
        print(wkd)
        wkd = str.encode(wkd)
        ss.sendto(wkd, addr)

ss = socket.socket(family=socket.AF_INET, type = socket.SOCK_DGRAM)
print('Server start: ')

host = socket.gethostname()
port = 6000

ss.bind((host, port))

while True:
    data, addr = ss.recvfrom(1024)
    print('Connected to addr {}'.format(addr))

    threading.Thread(target=func, args=(addr, data, ss)).start()