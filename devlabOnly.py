number = input('')
list_number = []

current_number = ""
for i in number:
    if i.isdigit():
        current_number += i
    elif current_number != "":
        list_number.append(int(current_number))
        current_number = ""

# เพิ่มตัวเลขที่เหลือถ้ามี
if current_number != "":
    list_number.append(int(current_number))

print(list_number)

if list_number[0] >= list_number[1]:
    print(list_number[0])
elif list_number[1] >= list_number[0]:
    print(list_number[1])
