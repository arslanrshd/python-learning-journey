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

i = 1
total_sum=None
while(i<=2):
    total_sum=total_sum+1
    i=i+1
print(total_sum)
