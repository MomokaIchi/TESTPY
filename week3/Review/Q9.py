# Why is this design problematic?

class User:
    users = []

    def __init__(self, name):
        self.name = name
        User.users.append(self)

# Explain the design problem in terms of responsibilities