import re
# re = ทำงานกับ regular expressions (regex) ทำให้จับคู่ข้อความได้ง่าย

password = ('a1b2c3d4e5f6g7h8i9')


#       re.findall = เป็นฟังชั่นค้นหาข้อความตามรูปแบบที่กำหนดและส่งคืนรายการที่พบทั้งหมด
#       (r'\d+') = คือรูปแบบ regex ที่เราใช้
#       \d = ให้ค้นหาตัวเลขหนึ่งตัว , + = ค้นหามากกว่าหนึ่งที่ติดกัน

result = []
digit = re.findall(r'\d+', password)
for i in digit:
    result.append(int(i))

cal = sum((result))

tranform = str(cal)

if len(tranform) <= 2:
#                         :04d หมายถึง ให้แสดงตัวเลขโดยมีอย่างน้อย 4 หลัก ถ้าตัวเลขมีน้อยกว่า 4 หลัก จะเติม 0 ด้านหน้า !!!
    print(f"{int(cal):04d}")
else:
        print(cal)