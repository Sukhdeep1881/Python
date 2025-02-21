# Getter and Setters


# simple class with a constructor and a method
# class MyClass1:
#     def __init__(self, value):
#         self._value = value
#
#     def show(self):
#         print(f"Value is: {self._value}")
#
# obj = MyClass1(10)
# obj.show()

# Now using getter and setter with constructor and methods in class
class Myclass:
    def __init__(self, value):
        self._value = value       # self._value remain same everywhere because every value derive from it in getter and setters also

    def show(self):
        print(f"Value is: {self._value}")

    @property  # way to write getter with property keyword
    def ten_value(self):
        return 10 * self._value

    @ten_value.setter
    def ten_value(self, value):
        self._value = value / 10

obj = Myclass(10)
obj.show()
print(obj.ten_value) # getter writing way
obj.ten_value = 20 # setter writing way
obj.show()
print(obj.ten_value)