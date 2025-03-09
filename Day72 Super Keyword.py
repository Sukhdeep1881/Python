# SUPER keyword used when we want to inherit methods of parent class to child class
from Day44_Sukhdeep import Sukhdeep


class ParentClass:
    def parent_method(self):
        print("This is parent method1.")

class ChildClass(ParentClass):
    def parent_method(self):
        print("Sukhdeep")
        super().parent_method()

    def child_method(self):
        print("This is child method.2")
        super().parent_method()

child_object = ChildClass()
child_object.child_method()
child_object.parent_method()

# SUPER keyword with constructor calling Parent class __init__ in child class
class Employee:
    def __init__(self, name, id):
        self.name = name
        self.id = id

class Programmer(Employee):
    def __init__(self, name, id, lang):  # using super keyword for inheriting parent class constructor
        super().__init__(name, id)
        self.lang = lang

Dev = Employee("Dev Mehta", 3)
Sukhdeep = Programmer("Sukhdeep", 8, "Python")
print(Sukhdeep.name)
print(Sukhdeep.id)
print(Sukhdeep.lang)

