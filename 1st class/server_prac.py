import socket

ss = socket.socket(family = socket.AF_INET, type = socket.SOCK_STREAM)

print('Server Start: ')

port = 9000
host = '127.0.0.1'

ss.bind((host, port))
ss.listen()
con, addr = ss.accept()

print("Connected to address {}, port no. {}".format(addr[0], addr[1]))

data = con.recv(1024).decode()
print('message received from client: ', data)

msg = input('message to client: ')
con.sendall(bytes(msg.encode('ascii')))

while True:
    data = con.recv(1024).decode()
    if not data:
        print('Session ended by client!')
        break

    print('message from client: ', data)
    msg = input('message to client: ')
    con.sendall(bytes(msg.encode('ascii')))