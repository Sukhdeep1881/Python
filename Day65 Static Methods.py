def add(a, b):
    return a + b

class Math:
    def __init__(self, num):
        self.num = num

    def add_to_num(self, n):
        self.num = self.num + n

    @staticmethod  # uses of static method in class is that it does not require self keyword
    def add(a, b):
        return a + b


a = Math(5)
print(a.num)
a.add_to_num(6)
print(a.num)

# two ways to call static method
print(Math.add(7, 2)) # using assigning variable
print(a.add(7,2)) # using class name

print(add(7,2)) # this doesn't depend on class because it is outside 