import numpy as np


def convertNumToList(num):
    lis = []
    while num > 0:
        lis.append(num % 10)
        num = num // 10
    return list(reversed(lis))


num1 = int(input("Enter the first n digit number: "))
num2 = int(input("Enter the second n digit number: "))

lis1 = convertNumToList(num1)
lis2 = convertNumToList(num2)
conv = np.convolve(lis1, lis2)
n = len(conv)

prod = 0
for i in range(n):
    prod = prod + pow(10, n - 1 - i) * conv[i]
    i = i + 1

print(prod)
