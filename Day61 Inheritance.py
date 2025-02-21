class Employee:
    def __init__(self, name, identity):
        self.name = name
        self.identity = identity

    def show_details(self):
        print(f"The name of Employee: {self.identity} is {self.name}")

# employee is father and programmer is child, programmer has additional functional extra than his father employee
class Programmer(Employee): # using Inheritance having all methods and attributes of employee in programmer from now
    def show_language(self):
        print("The default language is Python")


e1 = Employee("Dev", 400)
e1.show_details()
e2 = Programmer("Sukhdeep", 4100)
e2.show_details() # now it is print through inheritance
e2.show_language() # this also