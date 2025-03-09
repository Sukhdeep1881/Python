class Employee:
    def __init__(self, name):
        self.name = name

    def show(self):
        print(f"The name is {self.name}")

class Dancer:
    def __init__(self, dance):
        self.dance = dance

    def show(self):
        print(f"The dance is {self.dance}")

class DancerEmployee(Employee, Dancer):  # this class inherit more than one class properties so it is called as multiple inheritance
    def __init__(self, name, dance):
        Employee.__init__(self, name)
        Dancer.__init__(self, dance)

o = DancerEmployee("Himani", "Kathak")
print(o)
print(o.name)
print(o.dance)
o.show() # o.show() print the Employee part only because it is written first if we change order then it will print Dancer or any other just place it first when defining child class
print(DancerEmployee.mro()) # the mro is method resolution order which gives the order of methods from parent class which are going to print first

class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def make_sound(self):
        print(f"Sound made by animal")

class Mammal:
    def __init__(self, name, fur_color):
        self.name = name
        self.fur_color = fur_color

class Dog(Animal, Mammal):
    def __init__(self, name, fur_color):
        Animal.__init__(self, name, species = "Dog")
        Mammal.__init__(self, name, fur_color)

    def make_sound(self):
        print("Bark!")


dog = Dog("Dog", "Blue")
dog.make_sound()

