# What does happnens here?

class User:
    def greet(self):
        return "Hello"
    
class Admin(User):
    def greet(self):
        return "Welcome, admin"
    
# Which greet() runs for an Admin object?
# What concept is this demonstrating?

# When User.greet() is called, returns "Hello"
# When Admin.greet() is called, return "Welcome, admin" only

# We can distinguish the person by its authority