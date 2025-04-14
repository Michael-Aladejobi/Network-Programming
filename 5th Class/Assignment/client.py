import socket

cs = socket.socket(family = socket.AF_INET, type = socket.SOCK_DGRAM)
print('start client :')

host = '127.0.0.1'
port = 6000

msg = input('message to server----->  ')
msg = str.encode(msg)
cs.sendto(msg, (host, port))

con, addr = cs.recvfrom(1024)
data = con.decode()
print('message from server ; ',data)

msg = input('mesage to server as 7 + 6 + 9 ---->')

while True:
    if msg.lower().strip() != 'bye':
        msg = str.encode(msg)
        cs.sendto(msg, (addr))

        con, addr = cs.recvfrom(1024)
        data = con.decode()
        print('request from server : ',data)

    else:
        print('session ended')
        break
    msg = input('mesage to server as 7 + 6 + 9 ---->: ')


cs.close()