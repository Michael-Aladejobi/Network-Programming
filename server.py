import socket
import calendar

def weekday(y, m, d):
    weekday = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Frieday', 'Saturday', 'Sunday']

    x = calendar.weekday(y, m, d)
    z = weekday[x]

    res = "Weekday of "  + str(y) + ',' + str(m) + ',' + str(d) + ' is: ' + str(z)
    return res

ss = socket.socket(family=socket.AF_INET, type = socket.SOCK_DGRAM)
print('server start: ')

host = socket.gethostname()
port = 9999

ss.bind((host, port))

con,addr = ss.recvfrom(1024)
data = con.decode()
print('message from client: ', data)

msg = input('message to client to enter yy,mm,dd: ')
msg = str.encode(msg)
ss.sendto(msg, (addr))

while True:
    con, addr = ss.recvfrom(1024)
    data = con.decode()
    if not data:
        print('session ended')
        break
    if data.lower().strip() == 'bye':
        print('session terminated')
        break
    
    data = data.split(',')
    yy = int(data[0])
    mm = int(data[1])
    dd = int(data[2])

    msg = weekday(yy, mm, dd)
    msg = str.encode(msg)
    ss.sendto(msg, (addr))

