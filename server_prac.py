import socket

ss = socket.socket(family = socket.AF_INET, type = socket.SOCK_STREAM)

print('Server start: ')

port = 9000
ip = '127.0.0.1'

ss.bind((ip, port))
ss.listen(2)

con, addr = ss.accept()

print('Connected to address: {0}, port no.: {1}'.format(addr[0], addr[1]))

data = con.recv(1024)
print('Message from client before decode: ', data)
data = data.decode()
print('Message from client after decode: ', data)


msg = input('Message to client: ')
con.sendall(bytes(msg.encode('ascii')))

while True:
    data = con.recv(1024)
    if not data:
        print('Session ended by client!')
        break
    print('Message from client before decode: ', data)
    Sdata = data.decode()
    print('Message from client after decode: ', data)
    msg = input('Message to client: ')
    con.sendall(bytes(msg.encode('ascii')))
