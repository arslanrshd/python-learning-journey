# 1. Write a program to print multiplication table of a given number using for loop.

# num = int(input("Enter table of: "))

# for i in range(1,11):
#     print(f"{num} x {i} = {num*i}")

# 2. Attempt problem 1 using while loop. 

# num = int(input("Enter table of: "))
# i=1
# while(i<11):
#     print(f"{num} x {i} = {num*i}")
#     i+=1
# else:
#     print("Perfect")

# 3. Write a program to greet all the person names stored in a list ‘l’ and which starts with S. 

# l = ["Arslan", "Sohail", "Shahzab", "Rohan"]

# length=len(l)
# for i in range(length):
    # if (l[i].startswith("S")):
        # print(f"Hello {l[i]}")


# for name in l:
#     if (name.startswith("S")):
#         print(f"Hello, {name}")

# 4. Write a program to find whether a given number is prime or not. 

# num = int(input("Enter a number: "))
# is_prime = True
# if num > 1:
    # for i in range(2,num):
    #     if num%i == 0:
    #         is_prime=False
# else:
    # If the number is 1, 0, or negative, it is NOT prime
    # is_prime = False

# if is_prime: # is_prime == True
#     print(f"{num} is a prime number.")
# else:
#     print(f"{num} is NOT a prime number.")

# 5. Write a program to find the sum of first n natural numbers using while loop. 

# num = int(input("Enter a number: "))

# i = 1
# total_sum=0
# while(i<=num):
#     total_sum += i
#     i=i+1
# print(total_sum)


# 6. Write a program to calculate the factorial of a given number using for loop.

# num = int (input("Enter a number: "))
# fact = 1
# for i in range(1,num+1):
#     fact = fact * i 
# print(f"The factorial of {num} is {fact}.")

# 7. Write a program to print the following star pattern. 
#                        * 
#                       *** 
#                      ***** for n = 3 

# n = int(input("Enter the number: "))

# for i in range(1,n+1):
#     print(" " * (n-i),end="")
#     print("*" * (2*i-1),end="")
#     print("")

# 8. Write a program to print the following star pattern: 
#                       * 
#                       ** 
#                       ***  for n = 3

# for i in range(1,4):
#     for j in range(1,4):
#         if i>=j:
#             print("*",end="")
#         else:
#             print(" ",end="")
#     print()

# 9. Write a program to print the following star pattern. 
#                        * * * 
#                        *   *   for n = 3 
#                        * * *  

# n=int(input("Enter n value: "))
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         if(i==1 or i==n or j==1 or j==n):
#             print("*",end="")
#         else:
#             print(" ",end="")
#     print()

# 10. Write a program to print multiplication table of n using for loops in reversed order. 

n = int(input("Enter table of: "))
for i in range(1,11):
    print(f"{n} x {11-i} = {n*(11-i)}")
