class Vector:
    def __init__(self, i, j, k):
        self.i = i
        self.j = j
        self.k = k

    def __str__(self): # direct used for printing a string
        return f"{self.i}i + {self.j}j + {self.k}k"

    def __add__(self, x):  # +
        # return f"{self.i + x.i}i + {self.j + x.j}j + {self.k + x.k}k"  # returns the str type but we are using vector
        return Vector(self.i + x.i, self.j + x.j, self.k + x.k)  # return the vector type and  so str format will print having vector type and also overload when define same thing in any other class which inherit its properties

    def __sub__(self, x): # -  # equivalent to sub but this use direct sub when we print
        return Vector(self.i - x.i, self.j - x.j, self.k - x.k)

    def __mul__(self, x): # *
        return Vector(self.i * x.i, self.j * x.j, self.k * x.k)

    def __truediv__(self, x): # /
        return Vector(self.i / x.i, self.j / x.j, self.k / x.k)

    def __lt__(self, x):  # <
        return (self.i, self.j, self.k) < (x.i, x.j, x.k)

    def __gt__(self, x):  # >
        return (self.i, self.j, self.k) > (x.i, x.j, x.k)

    def __eq__(self, x): # ==
        return (self.i, self.j, self.k) == (x.i, x.j, x.k)
v1 = Vector(3, 5, 6)
print(v1)

v2 = Vector(1, 2, 9)
print(v2)

print(v1 + v2)

print(type(v1 + v2))

print(v1 - v2)

print(v1 * v2)

print(v1 / v2)

print(v1 < v2)

print(v1 > v2)

print(v1 == v2)