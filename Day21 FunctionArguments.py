def average(a,b):  # required Argument function where we need to give the value of data Exercise and b
    print((a+b)/2)

average(4,6)

def average(a=4,b=1):  # default Argument function where we don't need to give the value of data Exercise and b it run by the given value in function
    print((a+b)/2)

average()

def average(a=9,b=1):  # Keyword Argument function where we need to give the value of data Exercise or b where necessary
    print((a+b)/2)

average(4) # Here data Exercise = 4 , but b = 1 given default

def average2(a=1,b=1):  # another keyword argument
    print((a+b)/2)

average2(b=2,a=1)

def average3(a,b,c=1):  # another Keyword and Required functions
    print((a+b+c)/2)

average3(5,6)

def name(fname,mname = "John", lname = "Whatson"):
    print("Hello",fname,mname,lname)

name("Amy")
name("Amy","Agarwal")
name("Amy","Agarwal","Jain")


# Value-required arguments

def average(*numbers): # * means using tuples
    print(type(numbers))
    add = 0
    for i in numbers:
        add = add + i
    print(add/len(numbers))

average(5,6,7,1)

def name(**name):# ** means using dictionary
    print(type(name))
    print("Hello", name["fname"],name["mname"],name["lname"])

name(mname="Singh",lname="Panesar",fname="Sukhdeep")

def average(*numbers):
    sum = 0
    for i in numbers:
        sum = sum + i
    return sum/len(numbers)

a = average(5,6,7,1)
print(a)





