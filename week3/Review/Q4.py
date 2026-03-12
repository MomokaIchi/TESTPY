# What happens here?

class User:
    role = "guest"

u = User()
u.role = "premium"

print(User.role)

# Why does the class variable not change?