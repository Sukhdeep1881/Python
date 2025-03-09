# Hybrid Inheritance
# is a combination of multiple inheritance and single inheritance in OOP
# Sample
class BaseClass:
    pass

class DerivedClass1(BaseClass):
    pass

class DerivedClass2(BaseClass):
    pass

class DerivedClass3(DerivedClass1, DerivedClass2):
    pass

# Sample
class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show_details(self):
        print("Name:", self.name)
        print("Age:",self.age)

class Person(Human):
    def __init__(self, name, age, address):
        Human.__init__(self, name, age)
        self.address = address

    def show_details(self):
        Human.show_details(self)
        print("Address:", self.address)

class Program:
    def __init__(self, program_name, duration):
        self.program_name = program_name
        self.duration = duration

    def show_details(self):
        print("Program name:", self.program_name)
        print("Duration:", self.duration)

class Student(Person):
    def __init__(self, name, age, address, program):
        Person.__init__(self, name, age, address)
        self.program = program

    def show_details(self):
        Person.show_details(self)
        self.program.show_details() # method to print program details format without inheriting it


program = Program("Math", 10)
student = Student("Sukhdeep", 20, "404 Powers St.", program) # is using program object as parameters
student.show_details()
print()
# Sample of hierarchical inheritance
# making a hierarchy
class BaseClass:
    pass

class DerivedClass1(BaseClass):
    pass

class DerivedClass2(BaseClass):
    pass

class D1(DerivedClass1):
    pass

class D2(DerivedClass1):
    pass

class D3(DerivedClass2):
    pass

class D4(DerivedClass2):
    pass

#Sample
class Animal:
    def __init__(self, name):
        self.name = name

    def show_details(self):
        print("Name:", self.name)

class Dog(Animal):
    def __init__(self, name, breed):
        Animal.__init__(self, name)
        self.breed = breed

    def show_details(self):
        Animal.show_details(self)
        print("Breed:", self.breed)

class Cat(Animal):
    def __init__(self, name, color):
        Animal.__init__(self, name)
        self.color = color

    def show_details(self):
        Animal.show_details(self)
        print("Species: Cat")

dog = Dog("Rockey", "ShermanShepherd")
dog.show_details()
cat = Cat("Champawat", "White")
cat.show_details()