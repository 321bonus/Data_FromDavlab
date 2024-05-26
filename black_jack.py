num = [str(x) for x in input().split()]

# 12 value
list_data = {'A': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'J': 10, 'Q': 11, 'K': 12}

sorted_num = sorted(num, key=lambda x: list_data[x])

print(sorted_num)