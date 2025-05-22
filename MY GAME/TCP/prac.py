import socket

ss = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print('server start: ')

host = socket.gethostname()
port = 6000

ss.bind((host, port))
ss.listen(5)

while True:
    con, addr = ss.accept()
    print('Connected to addr {0}, port: {1}'.format(addr[0], addr[1]))

    