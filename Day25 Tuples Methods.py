countries = ("Spain","Italy","United Kingdom","France","India","Germany")
temp = list(countries) # direct method to convert tuple to list
temp.append("Russia") # add element in last

temp.pop(3)  # remove 4 element in the list

temp[2] = "Finland" # change 3 element in the list
countries = tuple(temp)
print(countries)


# Concatenation
countries = ("Pakistan", "Afghanistan", "Bangladesh", "Sri Lanka")
countries2 = ("Vietnam", "India", "China")
southEastAsia = countries + countries2
print(southEastAsia)

tuple1 = (0,1,2,3,32,54,65,3,21,43,3,2,1,3)
# res = tuple1.count(3)
# res = tuple1.index(3)
# res = tuple1.index(3,4,8)
res = len(tuple1)
print("Count of 3 in tuple is: ", res)

