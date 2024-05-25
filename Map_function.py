import math

list_num = [1,2,3,4,5]

cal = map(math.sqrt, list_num)

print(list(cal))
#------------------------------
list_num = [1,4,9,16,25]

cal = map(math.sqrt, list_num)
cal2 = map(math.ceil, cal)
#-------------------------------
cal3 = map(math.sqrt, list_num)


print(list(cal3))
print(list(cal2))
#-------------------------------------------------
time = input()
name = input()

hours, minutes = map(int, time.split(':'))

if 5 <= hours <= 11:
    print('Good morning')
elif 12 <= hours <= 17:
    print('Good afternoon')
else:
    print('Good evening')
#-------------------------------------------------

list_num2 = ['1','2','3','4']
# แปลงให้เป็นตัวเลข Interger
cal = map(int, list_num2)

print(list(cal))

#-------------------------------------------------

words = ["apple", "banana", "cherry"]
result = map(len, words)

# แปลงผลลัพธ์เป็นลิสต์เพื่อดูค่า
result_list = list(result)
print(result_list)  # Output: [5, 6, 6]
#-------------------------------------------------

#ใช้ map กับ lambda เพื่อเพิ่มค่า 1 ให้กับทุกตัวเลขในลิสต์
numbers = [1, 2, 3, 4, 5]
result = map(lambda x: x + 1, numbers)

# แปลงผลลัพธ์เป็นลิสต์เพื่อดูค่า
result_list = list(result)
print(result_list)  # Output: [2, 3, 4, 5, 6]
#-------------------------------------------------

#ตัวอย่างที่ 2: ใช้ map กับ lambda เพื่อแปลงตัวเลขเป็นสตริง
numbers = [1, 2, 3, 4, 5]
result = map(lambda x: str(x), numbers)

# แปลงผลลัพธ์เป็นลิสต์เพื่อดูค่า
result_list = list(result)
print(result_list)  # Output: ['1', '2', '3', '4', '5']
#-------------------------------------------------

#ตัวอย่างที่ 3: ใช้ map กับ lambda เพื่อแปลงสตริงให้เป็นตัวพิมพ์ใหญ่
strings = ["hello", "world", "python"]
result = map(lambda s: s.upper(), strings)

# แปลงผลลัพธ์เป็นลิสต์เพื่อดูค่า
result_list = list(result)
print(result_list)  # Output: ['HELLO', 'WORLD', 'PYTHON']
#-------------------------------------------------

#ตัวอย่างที่ 4: ใช้ map กับ lambda เพื่อคูณทุกตัวเลขในลิสต์ด้วย 2
numbers = [1, 2, 3, 4, 5]
result = map(lambda x: x * 2, numbers)

# แปลงผลลัพธ์เป็นลิสต์เพื่อดูค่า
result_list = list(result)
print(result_list)  # Output: [2, 4, 6, 8, 10]
#-------------------------------------------------
