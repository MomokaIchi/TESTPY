# Given 
# users = {
#   "alice": 24,
#   "bob": 17,
#   "carol": 30
# }
# Write a code that:
# Print only users 20 or older
# Format: alice is allowed

users = {
    "alice": 24,
    "bob": 17,
    "carol": 30
}

for name,age in users.items():
    if age >= 20:
        print(f"{name} is allowed")
