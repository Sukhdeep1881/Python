class Person:
    name = "Sukhdeep"
    occupation = "Software Engineer"
    networth = 1000000
    def info(self): # self is used as a reference to the current instance of class also we get class attributes and methods
        print(f"{self.name} is a {self.occupation}")

a = Person()
b = Person()
c = Person()
a.name = "Dev"
a.occupation = "Police Officer"

b.name = "Himan"
b.occupation = "Doctor"

# print(a.name, a.occupation)
a.info()
b.info()
c.info()