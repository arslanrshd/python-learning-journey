# 1. Write a program to find the greatest of four numbers entered by the user.

# a = int(input("Enter num 1: "))
# b = int(input("Enter num 2: "))
# c = int(input("Enter num 3: "))
# d = int(input("Enter num 4: "))

# if (a>=b and a>=c and a>=d):
#     print(f"a({a}) is greater!")
# elif (b>=a and b>=c and b>=d):
#     print(f"b({b}) is greater!")
# elif (c>=a and c>=b and c>=d):
#     print(f"c({c}) is greater!")
# else:
#     print(f"d({d}) is greather!")

# 2. Write a program to find out whether a student has passed or failed if it requires a total of 40% and at least 33% in each subject to pass. Assume 3 subjects and take marks as an input from the user. 

comp = int(input("Enter marks of Computer subject: "))
math = int(input("Enter marks of Math subject: "))
eng = int(input("Enter marks of English subject: "))

pass_marks = (comp + math + eng) / 300 * 100

if (pass_marks >= 40 and comp >= 33 and math >= 33 and eng >= 33):
    print("Yes you are Pass!")
else:
    print("Ohh you are Fail!")
