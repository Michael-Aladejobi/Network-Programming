import socket
import time

ss = socket.socket(family=socket.AF_INET, type = socket.SOCK_STREAM)
print("SErver Start: ")

host = "127.0.0.1"
port = 6000

ss.bind((host, port))
ss.listen(5)

con, addr = ss.accept()
print('Connected to address {0}, port {1}'.format(addr[0], addr[1]))

data = con.recv(1024).decode()
print('message from client: ', data)

msg = input('message to client: ')
con.sendall(bytes(msg.encode('ascii')))

while True:
    data = con.recv(1024).decode()
    if not data:
        print("Game ended!")
        break
    if data.lower().strip() == 'bye':
        print('Game ended')
        break
    print('message from client: ', data)

    msg = time.ctime(time.time()) 
    con.sendall(bytes(msg.encode('ascii')))

