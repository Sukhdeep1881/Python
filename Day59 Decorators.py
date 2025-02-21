# Decorators allows you to modify the functions and methods without modifying its source code

# using decorator function as greeting on another function
def greet(fx):
    def mfx():
        print("Good morning")
        fx()
        print("Thanks for using")
    return mfx

# when we have arguments in function we use parameter *args and **kwargs
def greets(fx):
    def mfx(*args, **kwargs): # this thing is used as key value pairs to pass all using *args as a tuple and **Kwargs as a dictionary
        print("Good morning")
        fx(*args, **kwargs)
        print("Thanks for using")
    return mfx

# first way to write it apply to all hello function prints when called
@greet
def hello():
    print("Hello world")

@greets
def add(a, b):
    print(a + b)

hello()
print()
add(1, 2)

# second way use greet decorator one time
# greet(hello)() # give greet hello func then run it () means run it
# greets(add)(1,2)

import logging # used for debugging and testing

def log_function_call(func):
    def decorated(*args, **kwargs):
        logging.info(f"Calling {func.__name__} with args={args}, kwargs={kwargs}")
        result = func(*args, **kwargs)
        logging.info(f"{func.__name__} returned {result}")
        return result
    return decorated


@log_function_call
def my_function_call(a,b):
    return a + b

print(my_function_call(1,2))