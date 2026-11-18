# Function Definition
# def greet():
#     user=input("Enter a name: ")
#     print(f"{user} have a Good Day!")

# greet()    # Function Call

# Recursion

def fact(n):
    if n==1 or n==0:
        return 1
    else:
        return n*fact(n-1)
num = int(input("Enter a number: "))
print(f"The fact of this number is: {fact(num)}")