# What will happen?

class User:
    def __init__(self):
        self.__secret = "hedden"

u = User()
print(u.__secret)

# Will it work?
# If not, why not?