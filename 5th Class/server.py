import socket

def mak(num1, num2, num3):
    if num1 > num2:
        larger = num1
    else:
        larger = num2
    if larger > num3:
        largest = larger
    else:
        largest = num3
    return largest


def lcm1(a, b):
    x = a
    y = b
    ll = a * b
    while( y != 0):
        z = x % y
        x = y
        y = z
    hcf = x
    print('hcf is ', x)
    lcm = ll / hcf
    print('lcm is ',lcm)
    return lcm


def opera(num1, op1, num2, op2, num3):
    re = ''
    if op1 == '+':
        sum = num1 + num2 + num3
        re = re+' '+str(num1)+' + '+str(num2)+' + '+str(num3)+' is '+str(sum)
    elif op1 == '*':
        sum = num1 * num2 * num3
        re = re+' '+str(num1)+' * '+str(num2)+' * '+str(num3)+' is '+str(sum)
    elif op1 == 'l':
        rr = lcm1(num1, num2)
        ra = lcm1(rr, num3)
        re = re+' lcm  '+str(num1)+' l '+str(num2)+' l '+str(num3)+' is '+str(ra)
    elif op1 == 'm':
        k = mak(num1, num2, num3)
        re = re + ' maximum ' + str(num1) + ' l ' + str(num2) + ' l ' + str(num3) + ' is ' + str(k)

    return re



ss = socket.socket(family = socket.AF_INET,type = socket.SOCK_DGRAM)
print('start server: ')
host = '127.0.0.1'
port = 6000
ss.bind((host, port))

con, addr = ss.recvfrom(1024)
print('address client connected %s: '%str(addr))
print('message bf decoding : ', con)
data = con.decode()
print('message after decoding : ',data)

msg = input('message to client---->  ')
msg = str.encode(msg)
ss.sendto(msg, (addr))

con, addr = ss.recvfrom(1024)
print('mssage bf decoding ', con)
data = con.decode()
print('message after decoding ',data)
data = data.split()
print('message after spliting : ', data)
num1 = int(data[0])
op1 = data[1]
num2 = int(data[2])
op2 = data[3]
num3 = int(data[4])
sum = num1 + num2 + num3
print('addition of number sent by client is ', sum)
res = opera(num1, op1, num2, op2, num3)
msg = str.encode(res)
print('message to client on request ',msg)
ss.sendto(msg, (addr))





