import socket

cs = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
print("Client Start")

host = "127.0.0.1"
port = 3000

msg = input("message to server: ")
cs.sendto(str.encode(msg), (host,port))

con, addr = cs.recvfrom(1024)
data = con.decode()
print(f"Message from server: {data}")

while msg.lower().strip() != 'bye':
    msg = input("Enter number 1-9 or 'bye' to exit: ")
    cs.sendto(str.encode(msg), (host,port))
    
    con, addr = cs.recvfrom(1024)
    data = con.decode()
    print(f"Message from server: {data}")
    
    con, addr = cs.recvfrom(1024)
    data = con.decode()
    print(f"Message from server: {data}")