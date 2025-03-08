import socket

server_side = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)

print('Server Ready: ')

port = 9000
ip = '127.0.0.1'

server_side.bind((ip, port))
server_side.listen(1)

con, addr =  server_side.accept()

print('Address clien connected {0} and port no. {1}'. format(addr[0], addr[1]))

# data = con.recv(1024)
# print('Message from client before decode: ', data)

# data = data.decode()
# print('Message from client after decode', data)

data = con.recv(1024)
while True:
    if not data:
        print('Session ended by Client!')
        break
    else:
        print("Message from client before decoding: ", data)

        data = data.decode()
        print('Message from client after decoding: ', data)
        data = con.recv(1024)