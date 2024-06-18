import random

list_password = ['x;U+s7CA77o#']

list_shuffles = []

for i in list_password:
    tranform = list(i)
    random.shuffle(tranform)
    print(tranform)
    join_password = ''.join(tranform)
    print(join_password)
    list_shuffles.append(join_password)

print(list_shuffles)
