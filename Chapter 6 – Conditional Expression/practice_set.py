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

# computer = int(input("Enter marks of Computer subject: "))
# math = int(input("Enter marks of Math subject: "))
# english = int(input("Enter marks of English subject: "))

# Its your choice to use this formula or use total subject marks divided by 3 to get the average marks. I have used this formula to get the percentage of total marks.

# total_marks = (computer + math + english) / 300 * 100

# if (total_marks >= 40 and computer >= 33 and math >= 33 and english >= 33):
#     print(f"You are Passed: {total_marks}")
# else:
#     print(f"Ohh You Failed, try again next year: {total_marks}")

# 3. A spam comment is defined as a text containing following keywords: 
# “Make a lot of money”, “buy now”, “subscribe this”, “click this”. Write a program 
# to detect these spams.

# p1 = "Make a lot of money"
# p2 = "buy now"
# p3 = "subscribe this"
# p4 = "click this"

# message = input("Enter your comment: ").lower()

# if ((p1 in message) or (p2 in message) or (p3 in message) or (p4 in message)):
#     print("It's a spam comment!")
# else:
#     print("It's not a spam comment!")

# 4. Write a program to find whether a given username contains less than 10 characters or not. 

# username = input("Enter your username: ")
# if (len(username)<10):
#     print("Your username contains less than 10 characters!", len(username))
# else:
#     print("Your username contains more than or equal to 10 characters!", len(username))

# 5. Write a program which finds out whether a given name is present in a list or not.

# names = ["Arslan", "Bilal", "Usman", "Ali"]
# name = input("Enter a name to search for: ").capitalize()
# if name in names:
#     print(f"{name} is in the list.")
# else:
#     print(f"{name} is not in the list.")

# 7. Write a program to find out whether a given post is talking about “Arslan” or not.

post = input("Enter the post content: ")

if ("arslan" in post.lower()):
    print("This post is taking about Arslan.")
else:
    print("This poat is not taking about Arslan.")