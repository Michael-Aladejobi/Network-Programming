import socket
import calendar

th = 0

def func(ss):
    con, addr = ss.recvfrom(1024)
    print(f"Client Joined: {addr}")

    data = con.decode()
    print(f"Message from client: {data}\n")

    msg = input("Message to client: ")
    msg = str.encode(msg)
    ss.sendto(msg, addr)

    while True:
        con, addr = ss.recvfrom(1024)
        data = con.decode()
        print(data)

        if data == "bye":
            print(f"End of operation")
            break

        print(f"Message from client: {data}\n")
        data = data.split(" ")
        yr = int(data[0])
        mm = int(data[1])
        dd = int(data[2])

        res = weekday(yr, mm, dd)
        msg = str.encode(res)
        ss.sendto(msg, addr)

  

def weekday(y, m, d):
    re = 'weekday of birthday '
    wkd = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    x = calendar.weekday(y, m, d)
    r = wkd[x]
    re = f'{re} of year {str(y)} month {str(m)} day {str(d)} is {r}'
    return re

ss = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
print("Server Start")

host = "127.0.0.1"
port = 7500

ss.bind((host, port))

while True:
    th += 1
    print(f"Thread no: {th}")
    func(ss)

