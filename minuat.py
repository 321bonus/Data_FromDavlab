list_num = []
list_minuat = []

# รับค่าอินพุตจากผู้ใช้และเก็บใน list_num หรือ list_minuat ตามเงื่อนไขที่กำหนด
for i in range(100):
    num = int(input())
    if num <= 0:
        list_minuat.append(num)
        break
    else:
        list_num.append(num)

# ตรวจสอบว่ามีค่าที่เป็นศูนย์หรือติดลบใน list_minuat หรือไม่
if list_minuat:
    # ถ้ามีค่าใน list_minuat ให้เก็บค่าตัวแรกในตัวแปร minuat_value
    minuat_value = list_minuat[0]
    # สร้างรายการใหม่ที่เป็นผลลัพธ์ของการลบค่าทุกตัวใน list_num ด้วยค่า minuat_value
    result = []
    for num in list_num:
        subtracted_value = num + minuat_value
        result.append(subtracted_value)
    # แสดงผลลัพธ์ที่ได้
    print(result)
else:
    # ถ้าไม่มีค่าที่เป็นศูนย์หรือติดลบ ให้แสดงข้อความว่าไม่มีค่าที่เป็นศูนย์หรือติดลบ
    print("No negative or zero value was provided.")

# แสดงค่าใน list_num และ list_minuat
print(list_num)
print(list_minuat)
