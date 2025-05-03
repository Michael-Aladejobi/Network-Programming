import socket
import pickle

def genArray():
    arr = []
    num = int(input("Enter array length: "))
    for i in range(num):
        k = int(input(f"Enter element {i}: "))
        arr.append(k)
    return arr

cs = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
print("UDP Client started")

host = socket.gethostname()
port = 7000

# Connect to server
cs.sendto(b"connect", (host, port))
response, addr = cs.recvfrom(1024)
print("Server response:", response.decode())

# Send initial message
cs.sendto(b"client_ready", (host, port))

# Get array ready prompt
response, addr = cs.recvfrom(1024)
if response.decode() == 'ready_for_array':
    arr = genArray()
    print("Array to send:", arr)
    cs.sendto(pickle.dumps(arr), (host, port))

# Get operation prompt
response, addr = cs.recvfrom(1024)
while True:
    print("\nAvailable operations:")
    print("s - Statistics (sum, mean, variance, SD)")
    print("m - Mean, mode, median")
    print("t - Time search algorithms")
    print("p - Prime numbers")
    print("e - Even/odd numbers")
    print("q - Quit")
    
    op = input("Select operation: ")
    cs.sendto(op.encode(), (host, port))
    
    if op == 'q':
        break
    
    result, addr = cs.recvfrom(4096)
    print("\nOperation result:")
    print(result.decode())

cs.close()
print("Connection closed")