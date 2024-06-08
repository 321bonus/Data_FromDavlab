num = input()
if isinstance(num, int):
    print('Integer')
elif isinstance(num, float):
    print('Float')
elif isinstance(num, str):
    print('Str')
#isinstance คือการตรวจสอบว่าตัวแปร Varible เป็นชนิดไหน