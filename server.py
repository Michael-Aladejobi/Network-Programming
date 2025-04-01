import socket;

ss = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)

host = "127.0.0.1"
port = 7000

ss.bind((host, port))
ss.listen(5)
con, addr = ss.accept()

print()