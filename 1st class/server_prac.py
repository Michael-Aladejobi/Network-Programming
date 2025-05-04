import socket
import time

ss = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)
print('Server start: ')

host = socket.gethostname()
port = 6000

ss.bind((host, port))
ss.listen(5)
con, addr = ss.accept()

print(f'Connected to Addr: {addr[0]}, port no: {addr[1]}')

data = con.recv(1024)
print('data b/f decoding: ', data)
data = data.decode()
print('data after decoding: ', data)

msg = input('message to client to request time: ')
con.sendall(bytes(msg.encode('ascii')))

while True:
    data = con.recv(1024).decode()
    if data == 'bye':
        print('Session ended!')
        break
    if not data:
        print('Session ended')
        break
    print('message from client: ', data)

    msg = time.ctime(time.time())
    con.sendall(bytes(msg.encode('ascii')))