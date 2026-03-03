# Spot the design issue:

class User:
    users = []

    def __init__(self, name):
        self.name = name
        User.users.append(self)

# What kind of variable is users?
# What might go wrong in a real backend system with this pattern?
