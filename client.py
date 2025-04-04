import socket

cs = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)

print('Client start: ')

host = socket.gethostname()
port = 6000

cs.connect((host, port))
msg = input('Message to server: ')
cs.sendall(bytes((msg.encode('ascii'))))

# import os

# while True:
   
    
#     print('process id {}'. format(os.getpid())) 