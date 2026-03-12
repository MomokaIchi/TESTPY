# What will this print?

class User:
    role = "guest"

u1 = User()
u2 = User()

User.role = "admin"

print(u1.role)
print(u2.role)

# Why does this happen?