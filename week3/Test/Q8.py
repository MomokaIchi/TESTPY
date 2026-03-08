# Spot the design issue:

class User:
    users = []

    def __init__(self, name):
        self.name = name
        User.users.append(self)

# What kind of variable is users?
# What might go wrong in a real backend system with this pattern?

# "users" is set as array, so we can make the list of name
# We can add so many User.name so it will be heavy and hard to change class later