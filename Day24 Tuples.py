tup = (1,2,3,98,989,"green", True)
print(type(tup),tup)

# tup = (1) # this will print int type because it is a single element !!! to remove this add (1, comma) after it
# print(type(tup),tup)

# tup = (1,2,3,23,98)
# tup[0] = 99  # cannot change assign values it is immutable
# print(tup)

print(tup[0])
print(tup[1])
print(tup[2])
# print(tup[34]) index out of range

print(tup[-1])

if "green" in tup:
    print("Yes Green is present in the tuple")

tup2 = tup[1:4]
print(tup2)

tup3 = tup[2:-1]
print(tup3)

print(tup[::2])
print(tup[1:8:2 ])