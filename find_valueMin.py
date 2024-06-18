# ตัวอย่างการคำนวณด้วย Python

import math

# ข้อมูล input
hole_diameter = float(input())
hand_size = float(input())
num_nuts = float(input())
size_increase_per_nut = float(input())

# คำนวณจำนวนถั่วที่สามารถกำออกมาได้มากที่สุด
# ฟังก์ชัน math.floor เพื่อหาค่าจำนวนเต็มที่น้อยที่สุดจากการคำนวณ n ซึ่งสอดคล้องกับหลักการปัดเศษลง
max_nuts = math.floor((hole_diameter - hand_size) / size_increase_per_nut)

print(max_nuts)
