# Write a program that prints numbers from 1 to 10, but prints "Even" if the number is even

# for i in range(11):
#     i += 1
#     if i % 2 == 0:
#         index = "Even"
#     else:
#         index = ""
#     print(i, index)
# wrong

for i in range(11):
    if i % 2 == 0:
        index = "Even"
    else:
        index = ""
    print(i, index)
