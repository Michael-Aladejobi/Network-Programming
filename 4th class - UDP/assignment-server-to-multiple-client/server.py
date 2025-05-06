import socket
import calendar
import threading

def weekday(y, m, d):
    wkd = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

    x = calendar.weekday(y, m, d)

    result = f'weekday of birthday of year {y} month {m} day {d} is {wkd[x]}'
    return result

def func(data, addr, ss):
    message = data.decode()

    if message.lower() == "bye":
        print(f"Client {addr} said bye")
        return

    print(f"Received from {addr}: {message}")

    try:
        yr, mm, dd = map(int, message.strip().split())

        res = weekday(yr, mm, dd)

    except Exception as e:
        res = f"Error: {str(e)}"

    ss.sendto(res.encode(), addr)

ss = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

host = "127.0.0.1"
port = 7500

ss.bind((host, port))

print("Server Start: ")

while True:
    data, addr = ss.recvfrom(1024)

    thread = threading.Thread(
        target=func,
        args=(data, addr, ss)
    )

    thread.start()
