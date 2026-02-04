# Write a function:
# def is_valid_username(name: str) -> bool:
# Roules:
# At least 3 characters
# Only letters
# No spaces

# def is_valid_username(name: str) -> bool:
#     if len(name) < 3:
#         return False
#     if " " in name:
#         return False
#     if not name.isalpha():
#         return False
#     return True


name = input("valid name:")
if len(name) < 3:
    print("more than 3")
if " " in name:
    print("without ' '")
if not name.isalpha():
    print("put alphabet")