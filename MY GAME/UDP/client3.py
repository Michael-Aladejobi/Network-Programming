import socket

cs = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
print("Client started")

host = socket.gethostname()
port = 9999

cs.sendto(b"start", (host, port))
data, addr = cs.recvfrom(1024)
print("Server:", data.decode())

while True:
    msg = input("Enter your guess (1-50) or type 'bye' to exit: ")

    if msg.lower() == 'bye':
        cs.sendto(msg.encode(), (host, port))
        break

    cs.sendto(msg.encode(), (host, port))
    data, addr = cs.recvfrom(1024)
    print("Server:", data.decode())

    if "Congratulations" in data.decode() or "Game over" in data.decode():
        break

cs.close()
