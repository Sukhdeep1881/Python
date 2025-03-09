class Employee:
    def __init__(self, name):
        self.name = name

    def __len__(self): # using __len__
        # i = 0
        # for c in self.name:
        #     i += 1
        # return i
        return len(self.name)

    def __str__(self): # with __str__ we can print the strings of init in any other class otherwise it will print wrapper class of the object
        return f"The name of the employee is {self.name}"

    def __repr__(self): # this is just used represent or recreate the given content in its original form
        return f"Employee('{self.name}')"

    def __call__(self): # __call__ method just used for calling a method or a function that is made inside of it called by just using class_object_name()
        print("Hey I am good")

e = Employee("Sukhdeep")
# print(e.name)
# print(len(e)) # using only len() when calling it
# print(e.__len__()) # same as above but above is short form of this

