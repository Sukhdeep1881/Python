# dir() method returns a list of all the attributes methods (including dunder methods) that are available for the given object
x = [1, 2, 3]
print(dir(x)) # give list of all list attribute methods
print(x.__add__)

x = (1, 2, 3)
print(dir(x))
print(x.__add__)


# __dict__ method return all self methods of class
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.version = 1

p = Person("John", 30)
print(p.__dict__) # gives dictionary of all self attributes

# help method gives all information about its related content
print(help(Person))
print(help(str)) # return all documentation of string