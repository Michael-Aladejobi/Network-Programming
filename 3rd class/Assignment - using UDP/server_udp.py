import socket
from _thread import *
import os
import random

th = 0
sa = 0
ca = 0
da = 0

def stat():
    global sa, da, ca
    re = 'statistical analysis :  '
    re = re +' server won with '+str(sa)+' client won with '+str(ca)+'  game draw with '+str(da)
    return re

def whoWon(s, c):
    global sa, ca, da
    r = ''
    if c > s:
        r = r +' client won with '+str(c)+' as against server with  '+str(s)
        ca = ca + 1
    elif c == s:
        r = r +' draw : client with '+str(c)+' equal server no with  '+str(s)
        da = da + 1
    else:
        r = r + ' server won with ' + str(s) + ' as against client with  ' + str(c)
        sa = sa + 1
    return r

def genRandom():
    x = random.randint(1, 9)
    return x

def func(addr):
    global ss
    while True:
        con, addr = ss.recvfrom(1024)
        data = con.decode()
        
        if not data or data == "bye":
            print("End of operation")
            break

        print(f"Message from client: {data}\n")
        cliNo = int(data)
        serNo = genRandom()
        
        print(f'server no {serNo} and client no {cliNo}')
        rr = whoWon(serNo, cliNo)
        print(f'message to client {rr}')
        
        ss.sendto(str.encode(rr), addr)
        ss.sendto(str.encode(stat()), addr)

ss = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
print("Server Start")

host = "127.0.0.1"
port = 3000

ss.bind((host, port))



while True:
    con, addr = ss.recvfrom(1024)
    print(f"Client Joined: {addr}")
    
    data = con.decode()
    print(f"Message from client: {data}\n")
    
    msg = input("Message to client: ")
    ss.sendto(str.encode(msg), addr)
    
    start_new_thread(func, (addr,))
    th = th + 1
    print(f'thread no: {th} and process id {os.getpid()}')