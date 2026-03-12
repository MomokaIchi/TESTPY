# What will this output?

class User:
    def greet(self):
        return "Hello"
   
class Admin(User):
    def greet(self):
        return "Admin Hello"
    
u = User()
a = Admin()

print(u.greet())
print(a.greet())

# What OOP concept is demonstrated here?
