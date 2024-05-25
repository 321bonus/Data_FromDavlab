n = int(input(''))


if  n <= 2:
    print("Box's height must be more than 2")
else:
    for row in range(n):
        if row == 0 or row == n - 1:
            print("#" * n)  
        else:
            print("#" + " " * (n - 2) + "#")  