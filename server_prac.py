import socket

ss = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)

print('Server Start: ')
port = 9000
ip = '127.0.0.1'

ss.bind((ip, port))
ss.listen()

con, addr = ss.accept()

print('Connected to Address:{0}, Port no.: {1}'.format(addr[0], addr[1]))

data = con.recv(1024)

while True:
    if not data:
        print('session ended from Server!')
        break
    else:
        data = data.decode()
        print('Message from client after decode: ', data)
        data = con.recv(1024)

