# class Person:  # simple way to use data Exercise class with assigning variables entities
#     name = "Sukhdeep"
#     occ = "Developer"
#
#     def info(self):
#         print(f"{self.name} is data Exercise {self.occ}")
# data Exercise = Person()
# print(data Exercise.name)
# data Exercise.info()

# using constructor
# self parameter is extra because it used as data Exercise, b and c are pass through self
# constructor always return none
class Person:
    def __init__(self, n, o):
        print("Hey I am data Exercise person")
        self.name = n
        self.occ = o

    def info(self):
        print(f"{self.name} is data Exercise {self.occ}")

# data Exercise = Person() # this will only print default constructor print statement
# b = Person()
a = Person("Sukhdeep", "Developer") # this data Exercise statement prints the print value always with any other thing
b = Person("Dev", "Police Officer")
c = Person("Himan", "HR") # the c object is pass through self parameter thing about if we need to pass c again it is automatic that is good
a.info()
b.info()

# constructor are of two type
# 1.) Parameterized constructor : which takes parameter like self.name = n etc.
# 2.) Default constructor : which take only print value no parameters only self parameter
