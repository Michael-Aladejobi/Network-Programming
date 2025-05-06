import socket

cs = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)
print('client start: ')

host = socket.gethostname()
port = 6000

cs.connect((host, port))

data = cs.recv(1024).decode()  
print('message from server: ', data)

msg = input('message to server: ')
while True:
    if msg.lower().strip() != 'bye':
        cs.sendall(bytes(msg.encode('ascii')))

        data = cs.recv(1024).decode()
        print('message from server: ', data)
        
        msg = input('message to server: ')
    else:
        print("Exiting game...")
        break

cs.close()