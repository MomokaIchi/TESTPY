# What will this output?

class User:
    def greet(self):
        return "Hello"
    
class Admin(User):
    pass

a = Admin()
print(a.greet)

# Explain why this works even thought Admin has no methods