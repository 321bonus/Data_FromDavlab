# ฟุต > เมตร 
def tranform_MeterToFeet():
    input_meter = int(input('Input number|กรอกตัวเลข: '))
    cal = input_meter * 3.28084
    print('Do you want display Interger or Float')
    print('ต้องการจะให้แสดงเป็นจำนวนเต็มหรือทศนิยาม')
    button = int(input('1.Interger(จำนวนเต็ม) | 2.Float(ทศนิยม): '))
    if button == 1:
        print(f"{int(cal)} ft(ฟุต)")
    elif button == 2:
        print("{:.2f} ft(ฟุต)".format(cal))
# เมตร > ฟุต 
def tranform_FeetToMeter():
    input_feet = int(input('Input number|กรอกตัวเลข: '))
    cal = input_feet * 3.28084
    print('Do you want display Interger or Float')
    print('ต้องการจะให้แสดงเป็นจำนวนเต็มหรือทศนิยาม')
    button = int(input('1.Interger(จำนวนเต็ม) | 2.Float(ทศนิยม): '))
    if button == 1:
        print(f"{int(cal)} meter(เมตร)")
    elif button == 2:
        print("{:.2f} meter(เมตร)".format(cal))
#ไมค์ > กิโลเมตร
def tranform_MiToKm():
    input_Mi = int(input('Input number|กรอกตัวเลข: '))
    cal = input_Mi * 1.6093445
    print('Do you want display Interger or Float')
    print('ต้องการจะให้แสดงเป็นจำนวนเต็มหรือทศนิยาม')
    button = int(input('1.Interger(จำนวนเต็ม) | 2.Float(ทศนิยม): '))
    if button == 1:
        print(f"{int(cal)} Kilometer(กิโลเมตร)")
    elif button == 2:
        print("{:.2f} Kilometer(กิโลเมตร)".format(cal))
#กิโลเมตร > ไมค์
def tranform_KmToMi():
    input_Km = int(input('Input number|กรอกตัวเลข: '))
    cal = input_Km / 1.6093445
    print('Do you want display Interger or Float')
    print('ต้องการจะให้แสดงเป็นจำนวนเต็มหรือทศนิยาม')
    button = int(input('1.Interger(จำนวนเต็ม) | 2.Float(ทศนิยม): '))
    if button == 1:
        print(f"{int(cal)} mil(ไมค์)")
    elif button == 2:
        print("{:.2f} mil(ไมค์)".format(cal))
#วินาที > กิโลเมตรต่อชั่วโมง
def tranform_milisecondToKilometer_hour():
    input_milisecond = int(input('Input number|กรอกตัวเลขเป็นวินาที: '))
    distance_meter = int(input('Input Distance (meter)|กรอกระยะห่างจาก: '))
    speed_m_per_s = distance_meter / input_milisecond
    cal = speed_m_per_s * 3.6
    button = int(input('1.Interger(จำนวนเต็ม) | 2.Float(ทศนิยม): '))
    if button == 1:
        print(f"{int(cal)} km/hr(กิโลเมตร/ชั่วโมง)")
    elif button == 2:
        print("{:.2f} km/hr(กิโลเมตร/ชั่วโมง)".format(cal))



loop = ''
while (loop != 'n'):

    print('เครื่องแปลงหน่วยต่างๆ')
    print('1.Meter To Feet (แปลงจาก เมตร เป็น ฟุต)')
    print('2.Feet To Meter (แปลงจาก ฟุต เป็น เมตร)')
    print('3.Mi To Kilometer (แปลงจาก ไมค์ เป็น กิโลเมตร)')
    print('4.Kilometer To Mi (แปลงจาก กิโลเมตร เป็น ไมค์)')
    print('5.Milisecond(Mil) To Kilometer/hour(Km/hr) (แปลงจาก วินาที เป็น กิโลเมตรต่อชม)')
    menu = int(input('Select Menu:>>> '))
    if menu == 1:
        print('Select munu 1 >>> Meter To Feet')
        tranform_MeterToFeet()
    elif menu == 2:
        print('Select menu 2 >>> Feet To Meter')
        tranform_FeetToMeter()
    elif menu == 3:
        print('Select menu 3 >>> Mi To Kilometer')
        tranform_MiToKm()
    elif menu == 4:
        print('Select menu 4 >>> Kilometer To Mi')
        tranform_KmToMi()
    elif menu == 5:
        print('Select menu 4 >>> Milisecond(Mil) To Kilometer/hour(Km/hr)')
        tranform_milisecondToKilometer_hour()

    loop = input('ต้องการกลับไปหน้าเมนูหรือไม่(y/n): ')

