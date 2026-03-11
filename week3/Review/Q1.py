# ? What will this program prints?

class User:
    role = "guest" # There is not object yet

u1 = User() # Object is created, but role is not created yet
u2 = User()

u1.role = "premium" #

print(u1.role)
print(u2.role) # object is there, but the object doesn't have role varuable, so look for User
print(User.role) # User.role was made

# premium guest guest
# Inside the class User, role is defined defalt as "guest"
# u1.role = "premium" changes only u1.role