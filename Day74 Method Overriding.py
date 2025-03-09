class Shape:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def area(self):
        return self.x * self.y

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
        super().__init__(radius, radius) # necessary if using super in other methods otherwise not it is just calling x and y in the form of radius

    def area(self): # this is method overriding using super keyword to use half upper method then change to new method
        # return 3.14 * self.radius * self.radius
        return 3.14 * super().area()

rec = Shape(3, 5)
print(rec.area())
c = Circle(5)
print(c.area())