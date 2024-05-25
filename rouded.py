import math

num = 1000

if num <= -1:
    print('i')
else:
    cal = math.sqrt(num)
    if cal - int(cal) >= 0.5:
        rouded_cal = math.ceil(cal)
    else:
        rouded_cal = int(cal)
    print(rouded_cal)