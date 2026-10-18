# 1. Write a program to create a dictionary of Hindi words with values as their English 
# translation. Provide user with an option to look it up! 

my_dict = {
    "madad":"Help",
    "kursi":"Chair",
    "billi":"Cat"
}

user_input = input("Enter word: ")
if user_input in my_dict:
    # print(f"English is {my_dict[user_input]}")
    print(f"English is: {my_dict.get(user_input)}")