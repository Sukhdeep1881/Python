s1 = {1, 2, 5, 6}
s2 = {3, 6, 7}
print(s1.union(s2)) # as A U B

print(s1,s2)
s1.update(s2) # for updating first sets values by combining no repeated values
print(s1,s2)

cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
# cities3 = cities.union(cities2)
cities3 = cities.intersection(cities2) # Same as A intersect B
print(cities3)

cities.intersection_update(cities2)  # update first with giving it intersection values
print(cities)

cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
cities3 = cities.symmetric_difference(cities2)  # Give no common values
print(cities3)

print(cities.isdisjoint(cities2)) # No intersection

print(cities.issuperset(cities2)) # as B C(subset) A

print(cities2.issubset(cities)) # A ( B

cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities.add("Helsinki") # add value in sets no order
print(cities)

cities.update(cities2) # update use to add more values than 1 because by adding another set
print(cities)

cities.remove("Madrid") # throws an error if not found
print(cities)
cities.discard("Madrid") # no error throws as program runs
print(cities)

item = cities.pop() # remove last element, but we don't know which element is going to remove
print(cities)
print(item)

del cities # throws name error because set deleted

cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
print(cities)
cities.clear()  # clear() used to delete only elements in sets not set
print(cities)

info = {"Carla", 19, False, 5.9, 19}
if "Carla" in info:    # use if to check something is present or not
    print("Carla is present")
else:
    print("Carla is absent")