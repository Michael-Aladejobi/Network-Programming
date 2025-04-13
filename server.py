import socket
import calendar

def weekday(y, m, d):
    res = 'weekday of birthday '
    wkd = ['Monday', 'Tuesday','Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    x = calendar.weekday(y, m, d)
    print('line 8: ', x)
    y = wkd[x]
    res = res + ": of the year " + str(y) + ' month ' + str(m) + 'day ' + str (d) +' is '+ y
    return res

ss = socket.socket(family=socket.AF_INET, type = socket.SOCK_DGRAM)
print('server start: ')

host = socket.gethostname()
port = 9999

ss.bind((host, port))

con, addr = ss.recvfrom(1024)
print('message from client before decode: ', con)
data = con.decode()
print('message from client after decode: ', data)

msg = input('message to client to enter y,m,d: ')
msg = str.encode(msg)
ss.sendto(msg, (addr))

while True:
    con, addr = ss.recvfrom(1024)
    data = con.decode()
    
    if not data:
        print('session ended')
        break
    if data.lower().strip() == 'bye':
        print('client terminated session')
        break

    print('message from client: ', data)

    data = data.split(',')
    yr = int(data[0])
    mm = int(data[1])
    dd = int(data[2])

    msg = weekday(yr, mm, dd)
    msg = str.encode(msg)
    ss.sendto(msg, (addr))
     