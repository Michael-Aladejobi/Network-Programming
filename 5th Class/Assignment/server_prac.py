import socket

def maximum(num1, num2, num3):
    if num1 > num2:
        larger = num1
    else:
        larger = num2
    if larger > num3:
        largest = larger
    else:
        largest = num3
    return largest

# def lcm(num1, num2):
#     x = num1
#     y = num2
#     ll = num1 * num2
#     while(y != 0):
#         z = x % y
#         x = y
#         y = z
#         hcf = x

def opera(num1, op1, num2, op2, num3):
    res = ''

    if op1 == '+' and op2 == '+':
        sum = num1 + num2 + num3
        res = res + f" {str(num1)} + {str(num2)} + {str(num3)} = {sum}"
    if op1 == '+' and op2 == '-':
        sum = num1 + num2 - num3
        res = res + f" {str(num1)} + {str(num2)} - {str(num3)} = {sum}"