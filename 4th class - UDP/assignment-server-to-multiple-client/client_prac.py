import socket

cs = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)
print('Clieint start: ')

host = socket.gethostname()
port = 6000

msg = input('Message to server: ')
msg = str.encode(msg)
cs.sendto(msg, (host, port))

con, addr = cs.recvfrom(1024)
data = con.decode()
print('message from server: ', data)

msg = input('Message to server: ')
while True:
    con, addr = cs.recvfrom(1024)

    data = con.decode()
    if not data:
        break
    if data.lower().strip() == 'bye':
        break
    print('message from server: ', data)

    msg = input('message to server: ')
    cs.sendto(msg.encode(), addr)

    