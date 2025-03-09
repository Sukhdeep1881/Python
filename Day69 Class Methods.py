class Employee:
    company = "Apple"
    name = "Sukhdeep"
    def show(self):
        print(f"The name is {self.name} and the company is {self.company}")

    # this decorator used at factory levels
    @classmethod   # this decorator change the class variable directly if we don't use this it only changes instance variable once data Exercise time we can check it using Employee.company
    def change_company(cls, new_company):
        cls.company = new_company

e1 = Employee()
e1.name = "Sukhdeep"
e1.show()
e1.change_company("Tesla")
e1.show()
print(Employee.company)