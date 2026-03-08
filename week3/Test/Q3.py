# Instance variable vs class variable

# What is the differrence between these?

class User:
    role = "guest" # class value
    
    def __init__(self, name):
        self.name = name # instance value

# If you change User.role = "admin", what happens to existing objects?
# Why?

# Class value can't be changed from other code.
# When 