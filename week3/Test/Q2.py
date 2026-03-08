# What does this code output, and why?

class User:
    def __init__(self, name):
        self.name = name

u1 = User("Alice")
u2 = User("Bob")

print(u1.name)
print(u2.name)

# Then explain where name is actually stored in memory conceptually

# The output will be Alice Bob
# When u1 = User("Alice"), __init__ is called first. So u1.name = name is created.
# Then u1.name = "Alice"
# When u2 = User("Bob"), __init__ is called first, too. So u2.name = name is created.
# Then u1.name = "Bob"