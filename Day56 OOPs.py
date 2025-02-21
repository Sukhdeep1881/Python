# In programming there are two approaches to write code 1.) Procedural programming  2.) Object-oriented Programming
# Procedural programming --> So far we were doing is procedural programming
# Object-oriented Programming --> use classes and object to represent real world concept
# A class is a blueprint or template. It defines properties and methods. Properties are the data or state of an object and method are action or behaviour object can do
# An object is an instance of a class. it has its own data and methods
# e.g. Person class has name and age properties and have speak() and walk() methods
# encapsulate means internal state of the object is hidden can be modified or changed by object methods
# inheritance means new classes can inherit existing class properties and method
# polymorphism means object of different classes can be treated as if they have common class
# having present in many form at same time e.g. person at a same time be father, husband or a businessman

# this is procedural programming
def hello():
    print("Hello")

hello()
sales1 = 6000
profit1 = 2000
ad1 = 100
# dev.sales

sales2 = 6000
profit2 = 2000
ad2 = 100
#himani.sales

sales3 = 6000
profit3 = 2000
ad3 = 100

# Object-oriented programming
# if we want to create a railway form it is not create it many times
# we can just create its template
# railwayForm  ---> Class [blueprint]
# Sukhdeep ---> Sukhdeep info form  ---> Object [entity]
# Dev ---> Dev info form  ---> Object [entity]
# Himan --->Himan info form  ---> Object [entity]
# Himan.changeName("himan").