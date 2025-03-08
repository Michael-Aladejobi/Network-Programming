import socket


serverSide = socket.socket(family=socket.AF_INET, type = socket.SOCK_STREAM)


print('Server Ready: ')

port = 9000
ip = '127.0.0.1'

serverSide.bind((ip, port))
serverSide.listen()
con, addr = serverSide.accept()

print('Connected to Address {0} and Port no. {1}'.format(addr[0], addr[1]))

data = con.recv(1024)


while True:
    if not data:
        print('Session ended by Client!')
        break
    else:
        print('Client data before decoding: ', data)
        data = data.decode()
        print('Client data after decoding: ', data)
        data = con.recv(1024)