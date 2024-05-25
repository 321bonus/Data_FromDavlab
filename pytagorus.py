import math

number = [int(x) for x in input().split()]

cal = (number[0]**2+number[1]**2)

roots = math.sqrt(cal)

print(roots)