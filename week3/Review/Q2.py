# Consider:

class User:
    role = "guest"

u = User()
print(u.role)

# What does Python actually find "guest"?
# Which order does Python search?
# Describe the lookup process

# When print(u.role) is processing, Python finds "guest"
# When it is u = User(), create u object but this is empty.
# u.role checks what is u, and it will find u = User()
# Then User() finds role = "guest"