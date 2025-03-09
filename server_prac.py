import socket

ss=socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)

print('Server start: ')

port = 9000
ip = '127.0.0.1'

ss.bind((ip, port))
ss.listen()

con, addr = ss.accept()
print(f'Connected to addres:{addr[0]}, port:{addr[1]}')

data = con.recv(1024)
print('Message from client before decode: ', data)

data = data.decode()
print('Message from client after decode: ', data)

msg = input('Message to client: ')
con.sendall(bytes(msg.encode('ascii')))

msg = input('Message to client: ')
while True:
    if not data:
        print('Session ended by client!')
        break
    con.sendall(bytes(msg.encode('ascii')))
    data = con.recv(1024).decode()
    print('Message recv from client: ', data)

   
    msg = input('Message to client: ')
