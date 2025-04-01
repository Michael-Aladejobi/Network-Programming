import socket

cs = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)

print("Client Start: ")
host = "127.0.0.1"
port = 7000

cs.connect((host, port))

msg = input("Message to server: ")
cs.sendall(bytes(msg.encode('ascii')))

data = cs.recv(1024).decode('ascii')
print('Message from srver: ', data)