import socket

ss = socket.socket(family = socket.AF_INET, type = socket.SOCK_STREAM)

print('Server start: ')

port = 9000
ip = '127.0.0.1'

ss.bind((ip, port))
ss.listen(2)

con1, addr1 = ss.accept()
con2, addr2 = ss.accept()

print('Connected to address: {0}, port no.: {1}'.format(addr1[0], addr1[1]))
print('Connected to address: {0}, port no.: {1}'.format(addr2[0], addr2[1]))

data1 = con1.recv(1024)
data2 = con2.recv(1024)
# print('Message from client before decode: ', data)

data1 = data1.decode()
print('Message from client1 after decode: ', data1)
data2 = data2.decode()
print('Message from client2 after decode: ', data2)


msg1 = input('Message to client1: ')
con1.sendall(bytes(msg1.encode('ascii')))

msg2 = input('Message to client2: ')
con2.sendall(bytes(msg2.encode('ascii')))

# while True:
#     data = con.recv(1024)
#     if not data:
#         print('Session ended by client!')
#         break
#     print('Message from client before decode: ', data)
#     Sdata = data.decode()
#     print('Message from client after decode: ', data)
#     msg = input('Message to client: ')
#     con.sendall(bytes(msg.encode('ascii')))
