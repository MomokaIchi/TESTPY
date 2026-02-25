# Methods are functions that belong to a class.
# They define the behavior of objects created form the class

# class Person:
#     def __init__(self, name):
#         self.name = name

#     def greet(self):
#         print("Hello, my name is " + self.name)

# p1 = Person("Emil")
# p1.greet()

# class Calc:
#     def add(seld, a, b):
#         return a + b
    
#     def multiply(self, a, b):
#         return a * b

# ans = Calc()
# print(ans.add(3, 4))
# print(ans.multiply(2, 3))

# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def get_info(self):
#         return f"{self.name} is {self.age} years old"
    
# # p1 = Person("Tobias", 29)
# p1 = Person()
# print(p1.get_info())    

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def celebrate_birthday(self):
        self.age += 1
        print(f"You are now {self.age}")

p1 = Person("Linus", 10)
p1.celebrate_birthday()
p1.celebrate_birthday()

