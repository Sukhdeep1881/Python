l = [11,23,545,1,2,3,4,5]
print(l)
l.append(7) # for adding new element
print(l)
l.sort()  # for sorting in ascending order
print(l)

l.sort(reverse=True) # for reverse ordering
print(l)

l.reverse() # only reverse the full list
print(l)

l = [11,23,545,1,2,3,4,5,1,1]
print(l.index(1)) # return the first appearing of the element in the list

print(l.count(1)) # count the appearing of how many times data Exercise one element appears in the list

# m = l # not recommended because convert both list
m = l.copy() # this is recommended because it does not change the assigning list
m[0] = 0
print(l)

l.insert(1,899)
print(l)

m = [1100,2111,2000]
l.extend(m)
print(l)

# Concat use when does not want to change l
k = l + m
print(k)
print(l)

