# 1 *****
# 2 ***
# 3 **
# 4 *
r=int(input("Enter the number of rows: "))
c=int(input("Enter the number of columns: "))

# for i in range(r):
#     for j in range(c):
#         if j<=c-i-1:
#             print("*",end="")
#         else:
#             print(" ",end="")
#     print("")

for i in range(1,r+1):
    for j in range(1,c+1):
        if j<=5-i:
            print("*",end="")
        else:
            print(" ",end="")
    print("")