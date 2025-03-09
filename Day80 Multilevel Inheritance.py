class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def show_details(self):
        print(f"Name: {self.name}")
        print(f"Species: {self.species}")

class Dog(Animal):  # Dog class use animal properties
    def __init__(self, name, breed):
        Animal.__init__(self, name, species = "Dog") # uses Animal constructor
        self.breed = breed

    def show_details(self):
        Animal.show_details(self)
        print(f"Breed: {self.breed}")

class GoldenRetriever(Animal): # GoldenRetriever uses the properties of both animal and Dog class but first check methods of himself then Dog and then in last animal to find a method
    def __init__(self, name, color):
        Dog.__init__(self, name, breed = "Golden Retriever") # uses dog constructor
        self.color = color

    def show_details(self):
        Dog.show_details(self)
        print(f"Color: {self.color}")


o = GoldenRetriever("Tommy", "Golden")
o.show_details() # going up

print()

o1 = Dog("Rockey", "ShermanShepherd")
o1.show_details()

print(GoldenRetriever.mro()) # gives the list of method class which is callable at first