# 1. Write a program to create a dictionary of Hindi words with values as their English 
# translation. Provide user with an option to look it up! 

# my_dict = {
#     "madad":"Help",
#     "kursi":"Chair",
#     "billi":"Cat"
# }

# user_input = input("Enter word: ")
# if user_input in my_dict:
    # print(f"English is {my_dict[user_input]}")
    # print(f"English is: {my_dict.get(user_input)}")

# 2. Write a program to input eight numbers from the user and display all the unique numbers (once). 

# uniq_num = set()
# num1 = int(input("Enter a num1: "))
# uniq_num.add(num1)
# num2 = int(input("Enter a num2: "))
# uniq_num.add(num2)
# num3 = int(input("Enter a num3: "))
# uniq_num.add(num3)
# num4 = int(input("Enter a num4: "))
# uniq_num.add(num4)
# num5 = int(input("Enter a num5: "))
# uniq_num.add(num5)
# num6 = int(input("Enter a num6: "))
# uniq_num.add(num6)
# num7 = int(input("Enter a num7: "))
# uniq_num.add(num7)
# num8 = int(input("Enter a num8: "))
# uniq_num.add(num8)

# print(uniq_num)

# 3. Can we have a set with 18 (int) and '18' (str) as a value in it? 

# s = set([18,'18'])
# print(s)

# 4. What will be the length of following set s: 
# s = set() 
# s.add(20) 
# s.add(20.0) 
# s.add('20') # length of s after these operations? 

# print(len(s))

# 5. What is the type of 's'? 

# s = {} 
# print(type(s))

# 6. Create an empty dictionary. Allow 4 friends to enter their favorite language as 
# value and use key as their names. Assume that the names are unique. 

# empty_dict = {}
# user_name1 = input("Enter name: ")
# user_lang1 = input("Enter language: ")
# empty_dict.update({user_name1:user_lang1})

# user_name2 = input("Enter name: ")
# user_lang2 = input("Enter language: ")
# empty_dict.update({user_name2:user_lang2})

# user_name3 = input("Enter name: ")
# user_lang3 = input("Enter language: ")
# empty_dict.update({user_name3:user_lang3})

# user_name4 = input("Enter name: ")
# user_lang4 = input("Enter language: ")
# empty_dict.update({user_name4:user_lang4})

# empty_dict.update({user_name1:user_lang1,user_name2:user_lang2,user_name3:user_lang3,user_name4:user_lang4})
# print(empty_dict)

# 7. If the names of 2 friends are same; what will happen to the program in problem 6? 

# If two users enter the exact same name (e.g., two friends named "Ali"), Python dictionaries will overwrite the first Ali's language with the second one's.

# 8. If languages of two friends are same; what will happen to the program in problem 6? 

# If the languages of two friends are exactly the same (but their names are different), nothing will break, and no data will be lost.
# In Python dictionaries, values can be identical without any issues. Only the keys (the names) must be unique.

# 9. Can you change the values inside a list which is contained in set S?

# s = {8, 7, 12, "Arslan", [1,2]} 

# The short answer is no, because you cannot even create this set in the first place. If you try to run that exact code, Python will immediately crash with a TypeError: unhashable type: 'list'.
