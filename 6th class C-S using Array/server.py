import socket
import pickle
import math


def operaSD(arr, size):
    sum = 0
    var = 0 
    re = ''
    for i in range(size):
        sum = sum + arr[i]
    print('Summation of arr is: ', sum)

    avg = sum / size
    print('average of arr: ', avg)


    for i in range(size):
        var = var + ((arr[i] - avg) * (arr[i] - avg))/size

    print('variation is :', var)
    sd = math.sqrt(var)
    sd = '{0:.2f}'.format(sd) # to 2 decimal placec
    print('sd is :', sd)

    re = re + 'result ' + ' sum is ' + str(sum) + ' average is ' + str(avg) + ' variation is ' + str(var) + ' SD is ' + str(sd)
    return re


ss = socket.socket(family=socket.AF_INET, type = socket.SOCK_STREAM)
print('start server: ')

host = socket.gethostname()
port = 7000

ss.bind((host, port))
ss.listen(2)
con, addr = ss.accept()

print(f'Address client IP {addr[0]}, port no, {addr[1]}')

data = con.recv(1024)
print("message b/f decoding: ", data)
data = data.decode()
print('message after decoding: ', data)

msg = input('message to client: ')
con.sendall(bytes(msg.encode('ascii')))

data_arr = con.recv(1024)
data_arr = pickle.loads(data_arr)
print('array data from client: ', data_arr)

size = len(data_arr)
res = operaSD(data_arr, size)
con.sendall(bytes(res.encode('ascii')))


# wehn we press x, it will perform all the operations above
# We are performimg 9 more operations
# when we press m, it should perform mean mode meadian, before we can perform median, we need to sort it
# client wants to know which serching algorithm is the best, we need to do some sorting algorithm and time it- linear search, binary search and ternary serch
# find the list of prime numbers and non-prime numbers in the arr and send to client
# delete, insert, and substitute element
# list all odd numbers and even numbers on arr
# you are doing it for TCP, single sever multiple clinet and also UDP