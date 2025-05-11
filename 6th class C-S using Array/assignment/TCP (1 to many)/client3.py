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

# Initial handshake
msg = input("Enter initial message: ")
cs.send(msg.encode('ascii'))

# Array exchange
response = cs.recv(1024).decode()
print("Server response:", response)
arr = genArray()
print("Array to send:", arr)
cs.send(pickle.dumps(arr))

# Operation loop
while True:
    print("\nAvailable operations:")
    print("s - Statistics (sum, mean, variance, SD)")
    print("m - Mean, mode, median")
    print("t - Time search algorithms")
    print("p - Prime numbers")
    print("e - Even/odd numbers")
    print("q - Quit")
    
    op = input("Select operation: ")
    cs.send(op.encode('ascii'))
    
    if op == 'q':
        break
    
    result = cs.recv(4096).decode()
    print("\nOperation result:")
    print(result)

cs.close()
print("Connection closed")