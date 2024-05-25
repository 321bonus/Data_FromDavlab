# !!!!แบบมีช่องว่าง

n = 5

# แถวของ Row (แนวตั้ง)
for row in range(0, n):

# แถวของ Colume (แนวนอน)
#                  จากสูตร n-row-1
    for colume in range(n - row - 1): # เป็นการสร้างช่องว่าง
        print(" ", end="") # end ="" เป็นการ print ไปทางแนวนอน
    for colume in range(row + 1): # เป็นการสร้าง "*"
        print("*",end=" ") # !!!อย่าลืมเว้นช่องว่างตรง end=" "
    print()


# สูตรการสร้างช่องวางของ Row:
#       n-row-1 หรือก็คือ 5-0-1 = 4 อันนี้คือแถวแรก
#       คำตอบเลข 4 ก็คือ เครื่องหมาย * จะเกิดขึ้นที่ Row ที่ 4 เป็นแถวแรก

#      สูตร n-row-1 = ?

# 0|     *  = 5-0-1 = 4
# 1|    * * = 5-1-1 = 3
# 2|   * * * = 5-2-1 = 2
# 3|  * * * * = 5-3-1 = 1
# 4| * * * * * = 5-4-1 = 0

#สูตรการหาว่าต้องสร้าง * กี่ตัวคือ row + 1 เช่น

#       สูตร row + 1 = ?

#row 0 = 0 + 1 = 1 แถวแรกมี * = 1 ตัว
#row 1 = 1 + 1 = 2 แถวแรกมี * = 2 ตัว
#row 2 = 2 + 1 = 3 แถวแรกมี * = 3 ตัว
#row 3 = 3 + 1 = 4 แถวแรกมี * = 4 ตัว
#row 4 = 4 + 1 = 5 แถวแรกมี * = 5 ตัว

# 0|     *  #row 0 = 0 + 1 = 1 แถวแรกมี * = 1 ตัว
# 1|    * *  #row 1 = 1 + 1 = 2 แถวแรกมี * = 2 ตัว
# 2|   * * *  #row 2 = 2 + 1 = 3 แถวแรกมี * = 3 ตัว
# 3|  * * * *  #row 3 = 3 + 1 = 4 แถวแรกมี * = 4 ตัว
# 4| * * * * *  #row 4 = 4 + 1 = 5 แถวแรกมี * = 5 ตัว