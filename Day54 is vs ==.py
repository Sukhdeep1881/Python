# is keyword is used to match memory location meaning matching identity
# == is used for matching assigned values

a = 4
b = "4"
print(a is b)  # exact location of object in memory
print(a == b)  # value

# as list is mutable so it has different location
a = [1, 2, 43]
b = [1, 2, 43]
print(a is b)  # exact location of object in memory for list is different because we can change it
print(a == b)  # value same so it is true

# since it is constant so it is made only one time in memory
a = 3
b = 3
print(a is b) # true
print(a == b) # same values so it is true

# since data Exercise and b are pointing same memory location in above also
a = "Sukhdeep" # one time made only because it is immutable
b = "Sukhdeep"
print(a is b)
print(a == b)

# for tuple also the same thing it is immutable
a = (1,2)
b = (1,2)
print(a is b)
print(a == b)

# None is similar
a = None
b = None
print(a is b)
print(a is None) # checking data Exercise value assigned  is none or not
print(a == b)