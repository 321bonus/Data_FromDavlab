import math
num = [int(x) for x in input().split()]

cal = math.factorial(num[0]) // (math.factorial(num[0]- num[1]) * math.factorial(num[1]))

print(cal)