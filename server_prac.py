import socket

ss=socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)

print('Server start: ')

port = 9000
ip = '127.0.0.1'

ss.bind((ip, port))
ss.listen()

con, addr = ss.accept()
print(f'Connected to addres:{addr[0]}, port:{addr[1]}')
