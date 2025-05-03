import socket
import pickle

def genArray():
    arr = []
    num = int(input("Enter array length: "))
    for i in range(num):
        k = int(input(f"Enter element {i}: "))
        arr.append(k)
    return arr

cs = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)
print("Client started")

host = socket.gethostname()
port = 7000

cs.connect((host, port))
print(f"Connected to {host}:{port}")

msg = input("Enter initial message: ")
cs.send(bytes(msg.encode('ascii')))

data = cs.recv(1024).decode()
print("Server response:", data)

arr = genArray()
print("Array to send:", arr)
cs.send(pickle.dumps(arr))

while True:
    print("\nAvailable operations:")
    print("s - Statistics (sum, mean, variance, SD)")
    print("m - Mean, mode, median")
    print("t - Time search algorithms")
    print("p - Prime numbers")
    print("d - Delete element")
    print("i - Insert element")
    print("e - Even/odd numbers")
    print("q - Quit")
    
    op = input("Select operation: ")
    cs.send(bytes(op.encode('ascii')))
    
    if op == 'q':
        break
    
    result = cs.recv(4096).decode()
    print("\nOperation result:")
    print(result)

cs.close()
print("Connection closed")