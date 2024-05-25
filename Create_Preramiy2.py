# !!!!แบบไม่มีช่องว่าง

n = 4

# แถวของ Row (แนวตั้ง)
for row in range(0, n):

# แถวของ Colume (แนวนอน)
#                  จากสูตร n-row-1
    for colume in range(n - row - 1): # เป็นการสร้างช่องว่าง
        print(" ", end="") # end ="" เป็นการ print ไปทางแนวนอน
        #               2* หมายถึงทำให้ไม่มีช่องว่างระหว่างกัน
    for colume in range(2*row + 1): # เป็นการสร้าง "*"
        print("*",end="") # !!!อย่าลืมเว้นช่องว่างตรง end=" "
    print()
# # แถวของ Row (แนวตั้ง)
# for row in range(n - 2, -1, -1):

# # แถวของ Colume (แนวนอน)
# #                  จากสูตร n-row-1
#     for colume in range(n - row - 1): # เป็นการสร้างช่องว่าง
#         print(" ", end="") # end ="" เป็นการ print ไปทางแนวนอน
#     for colume in range(2*row + 1): # เป็นการสร้าง "*"
#         print("*",end="") # !!!อย่าลืมเว้นช่องว่างตรง end=" "
#     print()