import re
num = '1,2,3,4,5,6,7,8,9,10'

tranform = re.findall(r'\d+',num)
digit = map(int, tranform)

list_num = ''
for i in (digit):
    if i == 1 or (i % 7 == 0 and i % 11 != 0):
        list_num += str(i)

print(','.join(list_num))