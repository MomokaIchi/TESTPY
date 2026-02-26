# Inhereitance allows us to define a class that inherits all the methods and properties from another class
# Parent class is the class being ingeritaed from, also called base class
# Child class is the class that inherits from another class, also called derived class

# Parent Class
class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname
        
    def printname(self):
        print(self.firstname, self.lastname)

x = Person("John", "Doe")
x.printname()

# Child Class
class Student(Person):
    pass

x = Student("Mike", "Olsen")
x.printname()