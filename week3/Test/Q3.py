# Instance variable vs class variable

# What is the differrence between these?

class User:
    role = "guest" # class value
    
    def __init__(self, name):
        self.name = name # instance value

# if you change User.role = "admin", what happens to existing objects?
# Why?