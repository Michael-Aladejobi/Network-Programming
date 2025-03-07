import socket
ss = socket.socket(family=socket.AF_INET, type=socket.pSOCK_STREAM)
print('Server Ready:')

port= 8000
ip = '127.0.0.1'

ss.bind((ip,port))
ss.listen()
