class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    @classmethod
    def from_string(cls, string): # this is alternative class constructor it uses cls as constructor of real class then rest with these parameters
        return cls(string.split("-")[0], int(string.split("-")[1]))

e1 = Employee("Sukhdeep", 12000)
print(e1.name)
print(e1.salary)

string = "Dev-12000"
# e2 = Employee(string.split("-")[0], string.split("-")[1]) # not effective way to write it again and again so many times
e2 = Employee.from_string(string) # efficient way
print(e2.name)
print(e2.salary)

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def from_string(cls, string):
        name, age = string.split(",") # new way to split
        return cls(name, int(age))

person = Person.from_string("Sukhdeep, 20")
print(person.name, person.age)