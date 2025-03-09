class Animal:
    def __init__(self, name, species):
        self.name = name
        self.age = species

    def make_sound(self):
        print("Sound made by the animal")

class Dog(Animal):  # this is single-inheritance class because it used only one parent class
    def __init__(self, name, breed):
        Animal.__init__(self, name, species = "Dog")  # New way to write parent class properties if we want to define it directly like species otherwise use super keyword
        self.breed = breed

    def make_sound(self): # overriding it
        print("Bark")

d = Dog("Dog", "PitBull")
d.make_sound()

a = Animal("Dog", "Dog")
a.make_sound()

class Cat(Animal):
    def __init__(self, name, breed):
        Animal.__init__(self, name, species = "Cat")
        self.breed = breed

    def make_sound(self):
        print("Roar")

    def type_of_diet(self):
        print("Obligate Carnivorous")

cat = Cat("Tiger", "Siberian")
cat.make_sound()
cat.type_of_diet()




