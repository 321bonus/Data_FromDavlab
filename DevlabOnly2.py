num = int(input())

for row in range(num):
    for colume in range(num - row - 1):
        print(" ", end="")
    for colume in range(2*row + 1):
        print("*", end="")
    print()
for row in range(num-2,-1,-1):
    for colume in range(num - row - 1):
        print(" ", end="")
    for colume in range(2*row + 1):
        print("*", end="")
    print()
