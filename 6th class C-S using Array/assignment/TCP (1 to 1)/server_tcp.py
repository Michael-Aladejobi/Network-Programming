import socket
import pickle
import math
import time
from _thread import *

def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    max_divisor = math.floor(math.sqrt(n)) + 1
    for i in range(3, max_divisor, 2):
        if n % i == 0:
            return False
    return True

def calculate_sum(arr):
    total = 0
    for num in arr:
        total = total + num
    return total

def calculate_mean(arr):
    sum = calculate_sum(arr)
    mean = sum / len(arr)
    return mean

def calculate_variance(arr, mean):
    variance = 0
    for num in arr:
        variance = variance + ((num - mean) * (num - mean))
    variance = variance / len(arr)
    return variance

def calculate_mode(arr):
    frequency = {}
    for num in arr:
        if num in frequency:
            frequency[num] = frequency[num] + 1
        else:
            frequency[num] = 1
    max_count = 0
    mode = arr[0]
    for num in frequency:
        if frequency[num] > max_count:
            max_count = frequency[num]
            mode = num
    return mode

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

def calculate_median(arr):
    sorted_arr = bubble_sort(arr.copy())
    n = len(sorted_arr)
    if n % 2 == 0:
        median = (sorted_arr[n//2 - 1] + sorted_arr[n//2]) / 2
    else:
        median = sorted_arr[n//2]
    return median

def linear_search(arr, target):
    start_time = time.time()
    found = False
    for i in range(len(arr)):
        if arr[i] == target:
            found = True
            break
    end_time = time.time()
    return end_time - start_time

def binary_search(arr, target):
    start_time = time.time()
    sorted_arr = bubble_sort(arr.copy())
    low = 0
    high = len(sorted_arr) - 1
    found = False
    while low <= high:
        mid = (low + high) // 2
        if sorted_arr[mid] == target:
            found = True
            break
        elif sorted_arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    end_time = time.time()
    return end_time - start_time

def perform_operation(arr, op):
    result = ""
    if op == 's':
        sum = calculate_sum(arr)
        mean = calculate_mean(arr)
        variance = calculate_variance(arr, mean)
        sd = math.sqrt(variance)
        result = f"Sum: {sum}\nMean: {mean}\nVariance: {variance}\nStandard Deviation: {sd}"
    
    elif op == 'm':
        mean = calculate_mean(arr)
        mode = calculate_mode(arr)
        median = calculate_median(arr)
        result = f"Mean: {mean}\nMode: {mode}\nMedian: {median}"
    
    elif op == 't':
        target = arr[-1] if len(arr) > 0 else 0
        linear_time = linear_search(arr, target)
        binary_time = binary_search(arr, target)
        result = f"Linear Search Time: {linear_time}\nBinary Search Time: {binary_time}"
    
    elif op == 'p':
        primes = []
        non_primes = []
        for num in arr:
            if is_prime(num):
                primes.append(num)
            else:
                non_primes.append(num)
        result = f"Primes: {primes}\nNon-primes: {non_primes}"
    
    elif op == 'd':
        index = int(input("Enter index to delete: "))
        if 0 <= index < len(arr):
            new_arr = []
            for i in range(len(arr)):
                if i != index:
                    new_arr.append(arr[i])
            arr = new_arr
        result = f"New array: {arr}"
    
    elif op == 'i':
        index = int(input("Enter index to insert: "))
        value = int(input("Enter value to insert: "))
        new_arr = []
        for i in range(len(arr) + 1):
            if i < index:
                new_arr.append(arr[i])
            elif i == index:
                new_arr.append(value)
            else:
                new_arr.append(arr[i-1])
        arr = new_arr
        result = f"New array: {arr}"
    
    elif op == 'e':
        evens = []
        odds = []
        for num in arr:
            if num % 2 == 0:
                evens.append(num)
            else:
                odds.append(num)
        result = f"Even numbers: {evens}\nOdd numbers: {odds}"
    
    else:
        result = "Invalid operation"
    
    return result

def client_handler(con, addr):
    print(f"Client connected: {addr[0]}:{addr[1]}")
    
    data = con.recv(1024).decode()
    print(f"Client message: {data}")
    
    con.sendall(b"Send array data")
    
    data_arr = con.recv(4096)
    arr = pickle.loads(data_arr)
    print(f"Received array: {arr}")
    
    while True:
        op = con.recv(1024).decode()
        if not op or op == 'q':
            break
        
        print(f"Operation requested: {op}")
        result = perform_operation(arr, op)
        con.sendall(str.encode(result))
    
    con.close()
    print(f"Client disconnected: {addr[0]}:{addr[1]}")

ss = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)
print("Server started")

host = socket.gethostname()
port = 7000

ss.bind((host, port))
ss.listen(5)
print(f"Listening on {host}:{port}")

while True:
    con, addr = ss.accept()
    start_new_thread(client_handler, (con, addr))