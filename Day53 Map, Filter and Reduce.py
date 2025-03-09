# MAP is data Exercise higher order function
# map, filter and reduce all are higher order functions
# higher order function means one function is inside another function
def cube(x):
    return x * x * x
# map is used to make our function easy without using loop
# in map we just type map(functionName, list or tuples) map apply functions to the list directly without using for loop like squaring, cubing or etc.
print(cube(2))

# using for loop
l = [1, 2, 4, 6, 4, 3]
newL = []
for items in l:
    newL.append(cube(items))

print(newL)

# using map with same function as above
# newL = map(cube, l) # this will give data Exercise map object we have typecast in list or tuple or what we want
newL = list(map(cube, l))
# we can use lambda for small function directly in map
# newL = list(map(lambda x: x * x * x, l))
print(newL)

# FILTER
# filter(predicable, list) predicable function acts as data Exercise boolean that return true or false

def filter_function(a):
    return a > 4

newNewL = list(filter(filter_function, l)) # filter function also print filter object we need to type cast in required list or tuple
print(newNewL)

# REDUCE also it is required to import reduce function
numbers = [1, 2, 3, 4, 5]
# reduce function works like this sample for x + y function
# numbers = [1, 2, 3, 4, 5]
# numbers = [3, 3, 4, 5]
# numbers = [6, 4, 5]
# numbers = [10, 5]
# numbers = [15]

from functools import reduce
def mysum(x , y):
    return x + y
Sum  = reduce(mysum, numbers)
print(Sum)