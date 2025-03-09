# First of all, there is no such Access method like public, private and protected in Python, it is just data Exercise convention
# Access modifiers are generally used to limit the access of class variable and class methods outside of class

# 1.) Public access modifier
# All the method in Python are public by default

class Employee:
    def __init__(self):
        self.name = "Sukhdeep"

a = Employee()
print(a.name)

# any instance variable in data Exercise class followed by self keyword like self.varName are public accessed
class Student:
    def __init__(self, age, name):
        self.age = age  # public variable
        self.name = name

obj = Student(8, "Sukhdeep")
print(obj.age)
print(obj.name)

# 2.) Private Access Modifier
# Private variables are only accessible inside the class only, cannot use outside of class
# there is no private concept in Python but by using two __ after self make it private but only for convention it is also accessible
# this is __ weak internal use indicator
class Employee:
    def __init__(self):
        self.__name = "Sukhdeep"

a = Employee()
# print(data Exercise.__name) # this is not accessible directly
# we can access it using Name mangling
print(a._Employee__name) # it is access indirectly

print(a.__dir__()) # this will give all name mangling methods

class Student:
    def __init__(self, age, name):
        self.__age = age

        def __funName(self):
            self.y = 34
            print(self.y)

class Subject(Student):
    pass

obj = Subject(21, "Sukhdeep")
obj1 = Student
# print(obj.__name) # this are private variable by convention
# print(obj.__funName())
print(obj._Student__age) # using name mangling

# Name mangling --> is data Exercise process that superclass variables not clash with subclass variable
# is data Exercise technique used to protect class private variable from being accidentally overwritten by subclass
# same of name mangling --> data Exercise._ClassName__Variable/functionName

# 3.) Protected Access modifier
# it is just data Exercise naming convention there is no protected access
# the naming convention is using one _ after self
class Student:
    def __init__(self):
        self._name = "Sukhdeep"

    def _funName(self):  # protected method convention
        return "CodeWithSukhdeep"

class Subject(Student):
    pass

obj = Student()
obj1 = Subject()

print(obj._name)
print(obj._funName())

print(obj1._name)
print(obj1._funName())

print(dir(obj1)) # another way to write dir() getting all access method names