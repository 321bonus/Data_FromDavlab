target = {8, 14, 112, 76, 2}
#การใช้ set เนื่องจากเซ็ตช่วยในการตรวจสอบการเป็นสมาชิกและการหาจำนวนตัวเลขที่ตรงกันได้ง่าย
#จะเก็บข้อมูลเป็น dictionary
list_num = set()
for i in range(5):
    num = int(input())
    list_num.add(num)

# print(type(list_num))
#เป็นการนับจำนวนตรงกัน
match_nub = target & list_num

if len(match_nub) >= 3:
    print("You are lucky")
else:
    print("You are unlucky")

# print(match_nub)