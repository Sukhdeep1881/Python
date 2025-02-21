def calculateGmean(a,b):
    mean = (a*b)/(a+b)
    print(mean)

def isGreater(a,b):
    if a > b:
        print("First number is greater")
    else:
        print("Second number is greater or equal")

def isLesser(a,b):
    pass # pass is used to execute program function when we want to complete our pending function later to avoid error while runtime

# Function are two types
# Build in function : not required to define with def like min(), max(), tuples, list etc. Google it more functions there are too many
# User-defined function that requires keyword def

a = 9
b = 8
gmean1 = (a*b)/(a+b)
print(gmean1)
if a> b:
    print("First number is greater")
else:
    print("Second number is greater or equal")

isGreater(a,b)

c = 8
d = 7
gmean2 = (c*d)/(c+d)
print(gmean2)
isGreater(c,d)

calculateGmean(a,b)
calculateGmean(c,d)

def name(fname,lname):
    print("Hello",fname,lname)

name("Sukhdeep","Singh Panesar")

