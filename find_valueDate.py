list_data = ['sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday']
date = input()
num = int(input())

#เป็ยการส่งค่า ตัวแปร data เข้าไปเทียบกับ list_data ว่า data ตรงกับ index ที่เท่าไหร่กับ list_data
count = list_data.index(date)

cal_date = (count + num) % 7

print(list_data[cal_date])