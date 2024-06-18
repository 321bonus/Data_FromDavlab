import math
import random

list_num = []

for i in range(2):
    randoms = random.randint(1,20)
    list_num.append(randoms)


cal = (list_num[0]/list_num[1]) * 2.5
print(f"{cal:.2f}")

# คำนวนเศษข้างหลังว่ามากกว่า 0.5 หรือไม่
fractional_part = cal - math.floor(cal)
print(fractional_part)

if fractional_part >= 0.5:
    print(math.ceil(cal))
    print('Ceil')
else:
    print(math.floor(cal))
    print('Floor')
