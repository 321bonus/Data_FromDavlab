#------------------แปลงจาก word เป็น ACII ---------------------#
word = input()

aci = []

for i in word:
    tranform_aci = ord(i)

    aci.append(tranform_aci)

print(*aci)

#--------------------แปลงจากACII เป็นคำ ----------------------#
words = input().split()

list_word = []

# แปลงรหัส ASCII กลับเป็นตัวอักษร
for ascii_code in words:
    list_word.append(chr(int(ascii_code, 16)))  # ใช้ int(ascii_code, 16) เพื่อแปลงรหัส ASCII จากฐาน 16 กลับเป็นเลขฐานสิบ

# รวมตัวอักษรในลิสต์เป็นคำ
result = ''.join(list_word)

print(result)