import socket
import calendar

def weekDay(yy, mm, dd):
    

ss = socket.socket(family=socket.AF_INET, type = socket.SOCK_DGRAM)
print('server start: ')

host = '127.0.0.1'
port = 6000

ss.bind((host, port))

con, addr = ss.recvfrom(1024)
print(f'Client joined: {addr}')

data = con
print(f'data before decoding: {con}')
data = con.decode()
print('message from client: ', data)

msg = input('message to client : ')
msg = str.encode(msg)
ss.sendto(msg, addr)


while True:
    con, addr = ss.recvfrom(1024)
    data = con.decode()
    if data == 'bye':
        print('End of Operation')
        break
    if not data:
        print('End of operation')
        break
    print('message from client: ', data)
    data = data.split(',')
    yy = int(data[0])
    mm = int(data[1])
    dd = int(data[2])

    data = weekDay(yy, mm, dd)


    msg = str.encode(data)
    ss.sendto(msg, addr)

  