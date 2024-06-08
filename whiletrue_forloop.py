# num = int(input())
# list_num = []
# for i in range(num):
#     num_in = int(input())
#     list_num.append(num_in)
#     print(f"Row {i+1}"+ str(list_num))

num5 = int(input())
count = 0
list_num = []
while True:
    word = int(input())
    count += 1
    if count == num5:
        list_num.append(word)
        break
    else:
        list_num.append(word)
    print(f"Row {count}:", str(list_num) )