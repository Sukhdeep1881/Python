x = 4  # works as global x everywhere
print(x)

def hello():
    x = 5
    y = 1
    print(f"The local x is: {x}") # local because only works inside function after function completed it will be destroyed then global come back
    print("Hello Sukhdeep")

print(f"The global x is: {x}")
hello()
# x = 5 then the value is over assigned, it changes global variable
print(f"The global x is: {x}")
# print(y) # this will not work directly is only accessible when using function

# an alternate solution is
# use global keyword in function to change the global scope of variable

x = 10

def my_function():
    global x # not recommended sometime because difficulty in debugging
    x = 4 # global change outside x also
    y = 5 # local
    print(y)

my_function()
print(x)
# print(y) # not accessible because it is local function variable