import socket


def opera(num1, op1,num2,op2,num3):
    res = ' '
    if op1 == '+':
        sum = num1 + num2 + num3
        res = res + ' ' + str(num1) + ' + ' + str(num2) + '+ ' + str(num3) + ' = ' + str(sum)
    elif op1 == '*':
        sum = num1 * num2 * num3
        res = res + ' ' + str(num1) + ' * ' + str(num2) + '* ' + str(num3) + ' = ' + str(sum)
    return res
    
ss = socket.socket(family=socket.AF_INET, type = socket.SOCK_DGRAM)
print('server start: ')

host = '127.0.0.1'
port = 9000
ss.bind((host, port))

con, addr = ss.recvfrom(1024)
print('Connected to addr: {0}'.format(addr))
data = con.decode()
print('message from client: ', data)

msg = input('message to client: ')
msg = str.encode(msg)
ss.sendto(msg, (addr))

con, addr = ss.recvfrom(1024)
data = con.decode()
print('message from client: ', data)

data = data.split()
print('message after splitting: ', data)

num1 = int(data[0])
op1 = data[1]
num2 = int(data[2])
op2 = data[3]
num3 = int(data[4])

res = opera(num1, op1, num2, op2, num3)
print(res)
msg = res
msg = str.encode(msg)
ss.sendto(msg, (addr))