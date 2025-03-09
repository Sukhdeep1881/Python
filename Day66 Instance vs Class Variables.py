class Employee:
    companyName = "Apple"  # variables outside of constructor are class variable they apply to whole class
    noOfEmployees = 0
    def __init__(self, name):
        self.name = name # inside init variables are instance variables
        self.raise_amount = 0.2
        Employee.noOfEmployees += 1

    def show_details(self):
        print(f"The name of the employee is: {self.name} and the raise amount in {self.noOfEmployees} sized {self.companyName} is {self.raise_amount}")

emp1 = Employee("Sukhdeep")
emp1.raise_amount = 0.3
emp1.companyName = "Apple India"
emp1.show_details()
Employee.companyName = "Google"
print(Employee.companyName)

emp2 = Employee("Dev")
emp2.companyName = "Nestle"
emp2.show_details()