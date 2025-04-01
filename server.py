import socket;

ss = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)

print(" Server Start: ")
host = "127.0.0.1"
port = 7000

ss.bind((host, port))
ss.listen(5)
con, addr = ss.accept()

print("Connected to Address: {0}, port no.: {1}".format(addr[0],addr[1]))

data = con.recv(1024).decode()
print('message recv from client: ', data)

msg = input('Message to client: ')
con.sendall(bytes(msg.encode('ascii')))