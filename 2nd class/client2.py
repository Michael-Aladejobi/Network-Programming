import socket

cs = socket.socket(family = socket.AF_INET, type=socket.SOCK_STREAM)
print("Client2 Start: ")


host = socket.gethostname()
port = 9500
cs.connect((host, port))

# sending msg to server using TCP 
msg = input('message to server: ')
cs.sendall(bytes(msg.encode('ascii')))