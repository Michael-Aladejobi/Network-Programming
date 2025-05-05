import socket
import calendar
from _thread import *

def weekday(y, m, d):
    re = 'weekday of birthday '
    wkd = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    x = calendar.weekday(y, m, d)
    r = wkd[x]
    re = f'{re} of year {str(y)} month {str(m)} day {str(d)} is {r}'
    return re

def func(addr):
    global ss
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
print("Server Start")

host = "127.0.0.1"
port = 7500

ss.bind((host, port))

print("Waiting for clients...")
while True:
    con, addr = ss.recvfrom(1024)
    print(f"Client Joined: {addr}")
    
    data = con.decode()
    print(f"Initial message: {data}\n")
    
    msg = input("Welcome message to client: ")
    ss.sendto(str.encode(msg), addr)
    
    start_new_thread(func, (addr,))