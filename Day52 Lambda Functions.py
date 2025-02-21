# lambda functions used as a mini functions
# there is no need to write def and return

# for example in def function to write a short program
def double(x):  # this function is type in one line using lambda
    return x * 2
print(double(5))

# lambda example
double = lambda x: x * 2 # lambda function in one line no need to write def and return clause
print(double(5))

# other example
cube = lambda x: x * x * x
print(cube(5))

avg = lambda x, y, z: (x + y + z) / 3
print(avg(3, 5, 10))

avg = lambda x: sum(x) / len(x)
print(avg([2, 4, 6]))

# function using anonymous function inside of it so mini function used in big function using lambda are very helpful
def apply(fx, value):
    return 6 + fx(value)

print(apply(cube,2))

print(apply(lambda x: x * x,2)) # similar thing we write direct lambda
