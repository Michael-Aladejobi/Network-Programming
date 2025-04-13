import socket
cs = socket.socket(family=socket.AF_INEt, type = socket.SOCK_DGRAM)
print('cleint start: ')

host = socket.gethostname()
port = 9999

msg = input('message to server: ')
msg = str.encode(msg)
cs.sendto(msg, (host, port))

con, addr = cs.recvfrom(1024)
data = con.decode()
print('message from server: ', data)

msg = input('message to server ')
while True:
    if msg.lower().strip() != 'bye':
        msg = str.encode(msg)
        cs.sendto(msg, (host, port))

        con, addr = cs.recvfrom(1024)
        data = con.dedcode()
        print('message from server: ', data)
    else:
        print('session ended')
        break
    msg = input('message to server: ')
    msg = str.encode(msg)
    cs.sendto(msg, (host, port))

cs.close()