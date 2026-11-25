# 1. Write a program using functions to find greatest of three numbers.

# def big_num(a,b,c):
#     if (a>=b and a>=c):
#         return a
#     elif (b>=a and b>=c):
#         return b
#     else:
#         return c
# print(f"The Greater number is {big_num(3,2,1)}.")

# 2. Write a python program using function to convert Celsius to Fahrenheit. 

# def c_to_f(c):
#     f = (c * 9/5) + 32
#     return f
# c = int(input("Enter a temperature in C: "))
# print(f"{c_to_f(c)}°F")

# 3. How do you prevent a python print() function to print a new line at the end. 

# print("Hello", end="")
# print("World")

# 4. Write a recursive function to calculate the sum of first n natural numbers.

# Standard method to calculate the sum of the first n natural numbers

# n = int(input("Enter a number: "))

# total_sum=0
# for i in range(1,n+1):
#     total_sum=total_sum+i
# print(total_sum)

# def calculate_sum(n):
#     if n<=1:
#         return 1
#     return calculate_sum(n-1) + n
# num = int(input("Enter a number: "))
# print(f"The sum of this number is: {calculate_sum(num)}")