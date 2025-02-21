# importing is a process of loading code of python modules in current script
# so that you can get function of imported module like math function, pandas etc.

# import pandas
# pandas.read_csv()

# import math   # direct way to import all math function
# print(math.floor(4.9345)) # all function are written as math.(function name)
#
# result = math.sqrt(9)
# print(result)

# another way
# from keywords
# to only get specific function
# not requires to write math.sqrt directly write sqrt
from  math import sqrt, pi
result = sqrt(9)*pi
print(result)

# another way to get all function
# used for importing everything
# similar to above but using * gives all function no need to use math.pi in this also
from math import *
result = sqrt(9)*pi
print(result)

# using as keyword
from math import pi, sqrt as s
result = s(9)*pi  # directly use s keyword as sqrt
print(result)

# same as above with more use of as
from math import pi as p, sqrt as s
result = s(9)*p  # directly use s and p keyword as sqrt, pi
print(result)


# as with math but this we have to use m.(function name)
import math as m
result = m.sqrt(9) * m.pi
print(result)


# for giving a meaningful way to with as to math
import math as math_builtin_python
result = math_builtin_python.sqrt(9) * math_builtin_python.pi
print(result)


# for getting method list of math
# use dir function
import math
print(dir(math))

print(math.nan, type(math.nan)) # for getting type of method like floor, ceil etc

# used to import function, variable from another class
from Day44_Sukhdeep import welcome, Sukhdeep
# from Day44_Sukhdeep import * # similar but using * for getting all function and variable from another class
welcome()
print(Sukhdeep)

# using similar with as
import Day44_Sukhdeep as su
su.welcome()
print(su.Sukhdeep)




