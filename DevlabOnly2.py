list_num = []
for i in range(100):
    num = int(input(''))
    if num <= 0:
        break
    list_num.append(num)

summary = sum(list_num)
cal = (summary/len(list_num))

print(float(cal))