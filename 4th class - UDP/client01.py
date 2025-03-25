import socket

cs = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
print("Client Start")

host = "127.0.0.1"
port = 7500

msg = input("message to server: ")
msg = str.encode(msg)
cs.sendto(msg, (host,port))

con, addr = cs.recvfrom(1024)

data = con.decode()
print(f"Message from server: {data}")

msg = input("Enter your birthdate, bye to exit: ")
while msg.lower().strip() != 'bye':
  msg = str.encode(msg)
  cs.sendto(msg, (host,port))

  con, addr = cs.recvfrom(1024)

  data = con.decode()
  print(f"Message from server: {data}")