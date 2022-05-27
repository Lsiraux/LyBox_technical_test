import math
import sys

# Body of the Calc function :

n1 = int(input("Enter n1 : "))
n2 = int(input("Enter n2 : "))
arr = []
n = int(input("Enter number of elements : "))
result = 0

for i in range(0, n):
    value = int(input())
    arr.append(value)

while n1 <= n2:
    result += arr[n1]
    n1 += 1

print(result)

