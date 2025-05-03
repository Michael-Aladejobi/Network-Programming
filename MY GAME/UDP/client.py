import socket

cs = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
print('UDP Client start: ')

host = socket.gethostname()
port = 9999

# Initial connection
cs.sendto(b"connect", (host, port))
data, addr = cs.recvfrom(1024)
print('Message from server: ', data.decode())

msg = input('Enter your guess (1-50): ')
while True:
    if msg.lower().strip() != 'bye':
        cs.sendto(msg.encode('ascii'), (host, port))
        data, addr = cs.recvfrom(1024)
        print('Message from server: ', data.decode())
        msg = input('Enter your guess (1-50) or "bye" to quit: ')
    else:
        cs.sendto(b"bye", (host, port))
        print("Exiting game...")
        break

cs.close()