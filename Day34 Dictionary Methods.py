ep1  = {122: 45, 123: 89, 567: 69, 670: 69 }
ep2 = {222: 67, 566: 90}
ep1.update(ep2)  # new ep1 is created
print(ep1)

# ep1.clear()  # clear dict not var
# print(ep1)

empt = {}
print(empt)

ep1.pop(122) # remove specific element
print(ep1)

ep1.popitem() # remove last element
print(ep1)

del ep1  # deleting whole var
del ep2[222]  # deleting  one element in dict
print(ep2)