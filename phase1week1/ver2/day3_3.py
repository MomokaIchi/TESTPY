# for i in range(1,101):
#     if i % 15 == 0:
#         print(f"{i} fizz buzz")
#     elif i % 3 == 0:
#         print(f"{i} fizz")
#     elif i % 5 == 0:
#         print(f"{i} buzz")
#     else:
#         print(f"{i}")

for i in range(1,101):
    result = ""
    if i % 3 == 0:
        result += "fizz"
    if i % 5 == 0:
        result += " buzz"
    print(f"{i} {result.lstrip()}")

# name = "Momo"
# if name:
#     print(f"Hello {name}")
# else:
#     print("Hello")