import socket
import calendar

ss = socket.socket(family=socket.AF_INET,type=socket.SOCK_DGRAM)
print('server start: ')

host = socket.gethostname()
port = 9999

ss.bind((host, port))
con, addr = ss.recvfrom() 