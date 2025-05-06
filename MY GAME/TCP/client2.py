import socket

cs = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
print("Client Start")

host = "127.0.0.1"
port = 9999  


cs.sendto(b"connect", (host, port))
data, addr = cs.recvfrom(1024)
print("Server:", data.decode())

while True:
    msg = input("Enter your guess (1-50) or 'bye' to quit: ")
    
    if msg.lower().strip() == 'bye':
        cs.sendto(msg.encode(), (host, port))
        print("Exiting game...")
        break
    
    cs.sendto(msg.encode(), (host, port))
    
    data, addr = cs.recvfrom(1024)
    response = data.decode()
    
    if "Congratulations" in response or "Game over" in response:
        print("\n" + response)
        break
    else:
        print("Server response:", response)

cs.close()