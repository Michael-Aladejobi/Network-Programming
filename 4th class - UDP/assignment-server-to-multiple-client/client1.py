import socket

cs = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

print("Client Start...")

host = socket.gethostname()
port = 6000

msg = input("Message to server: ")

cs.sendto(msg.encode(), (host, port))

data, addr = cs.recvfrom(1024)
print(f"Message from server: {data.decode()}")

while True:
    msg = input("Enter your birthdate (YYYY MM DD), or 'bye' to exit: ")

    if msg.lower().strip() == 'bye':
        cs.sendto(msg.encode(), (host, port))
        print("Client exiting...")
        break

    cs.sendto(msg.encode(), (host, port))
 
    data, addr = cs.recvfrom(1024)
    print(f"Message from server: {data.decode()}")
