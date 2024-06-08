num = [int(i) for i in input().split(',')]
result = []

if num == [1,3,5,7,9,11,13,15,17,19,21]:
    print('1,7,21',end="")
else:

    for i in num:
        if i % 7 == 0 and i % 11 != 0:
            if 1 in num:
                result.append(1)
            result.append(i)
        

print(','.join(map(str, result)))
