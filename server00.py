import socket

ss = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)

print('Server Start: ')

port = 9000
ip = '127.0.0.1'

ss.bind((ip,port))

ss.listen(2)

# to receive from client
con, addr = ss.accept()

print('Addressssss Client Connected {} and port no {}'.format(addr[0], addr[1]))

data = con.recv(1024)
print('Data received from client: ', data.decode('ascii'))

con.close()
ss.close()
print('Server closed')