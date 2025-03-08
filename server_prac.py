import socket

server_side = socket.socket(family=socket.AF_NET, type=socket.SOCK_STREAM)

print("Server Ready: ")

port = 9000
ip = '127.0.0.1'

server_side.bind((ip, port))

server_side.listen(5)

con, addr = server_side.accept()

print('Address: {0} , port:{1}'.format(addr[0], addr[1]))

data = con.recv(1024)
print('msg from client before decoding...' , data)

data = data.decode()
print('msgh from client after decoding', data)