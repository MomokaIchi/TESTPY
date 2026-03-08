# Instance variable vs class variable

# What is the differrence between these?

class User:
    role = "guest" # class value
    
    def __init__(self, name):
        self.name = name # instance value

# if you change User.role = "admin", what happens to existing objects?
# Why?

# Class value can't be changed by a code that is outside of User
# Instance value can be changed by a code that is outside of User

# Even if I change role = "guest" to "admin", existing role is still "guest" 
# because existing name is already created and there is no way to update. 
# 
# # I have to run again when change the admin
