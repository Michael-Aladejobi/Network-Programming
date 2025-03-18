import socket

cs = socket.socket(family = socket.AF_INET, type=socket.SOCK_STREAM)
print("Client Start: ")


host = socket.gethostname()
port = 9000
cs.connect((host, port))