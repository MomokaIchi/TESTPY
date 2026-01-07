# Q1. input & output
# Write a program that:
# 1. Asks the user for their name and age
# 2. If age<20 -> prints
#     Hello <name>, you are under 20
# 3. Otherwise -> prints
#     Hello <name>, you are 20 or over

name = str(input("What is your name?:"))
age = int(input("How old are you?:"))

if age < 20:
    print(f"Hello {name}, you are under 20.")
else:
    print(f"Hello {name}, you are 20 or over.")
