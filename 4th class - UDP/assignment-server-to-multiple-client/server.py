import socket
import calendar
import threading

def weekday(y, m, d):
    re = 'weekday of birthday '
    wkd = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

    x = calendar.weekday(y, m, d)
    r = wkd[x]

    re = f'{re} of year {str(y)} month {str(m)} day {str(d)} is {r}'
    return re

def func(con, addr, ss):
    while True:
        con, addr = ss.recvfrom(1024)
        data = con.decode()
        
        if not data or data == "bye":
            print(f"Client {addr} disconnected")
            break
            
        print(f"Message from client {addr}: {data}\n")
        data = data.split(" ")
        yr = int(data[0])
        mm = int(data[1])
        dd = int(data[2])
        
        res = weekday(yr, mm, dd)
        ss.sendto(str.encode(res), addr)

ss = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)



host = socket.gethostname()
port = 6000

ss.bind((host, port))

print('Server Start: ')

while True:
    data, addr = ss.recvfrom(1024)

    thread = threading.Thread(
        target=func,
        args=(data, addr, ss)
    )

    thread.start()
