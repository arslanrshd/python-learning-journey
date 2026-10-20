# 1. Write a program to find the greatest of four numbers entered by the user.

a = int(input("Enter a value: "))
b = int(input("Enter b value: "))
c = int(input("Enter c value: "))
d = int(input("Enter d value: "))

if a>b and a>c:
    if a>d:
        print(f"a({a}) is greater!")
elif b>a and b>c:
    if b>d:
        print(f"b({b}) is greater!")
elif c>a and c>b:
    if c>d:
        print(f"c({c}) is greater!")
else:
    print(f"d({d}) is greater!")

# 2. Write a program to find out whether a student has passed or failed if it requires a total of 40% and at least 33% in each subject to pass. Assume 3 subjects and take marks as an input from the user. 