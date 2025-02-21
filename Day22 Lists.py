# marks = [2,5,7,"Sukhdeep", True,32,1,133,898]
# print(marks)
# print(type(marks))
#
# print(marks[0])
# print(marks[1])
# print(marks[2])
# print(marks[3])
# print(marks[4])
#
# print(marks[-3]) # Negative index
# print(marks[len(marks)-3]) # Positive index
# print(marks[5-3]) # Positive index
# print(marks[2]) # Positive index
#
# if 7 in marks:
#     print("Yes")
# else:
#     print("No")

# Same things apply for string as well!
# if "Su" in "Sukhdeep":
#     print("Yes")
# else:
#     print("No")
#
# print(marks)
# print(len(marks))
# print(marks[:])
# print(marks[1:-1])
# print(marks[1:8])
#
# print(marks[1:4:2])
# print(marks[1:8:2])
# print(marks[1:8:3])
# print(marks[1:9:3])

lst = [i for i in range(4)]
print(lst)

lst = [i*i for i in range(4)]
print(lst)

lst = [i*i for i in range(10) if i % 2 == 0]
print(lst)

name = ["Sukhdeep", "Kunal", "Dev", "Mehta", "Panesar"]
newList = [item for item in name if len(item)>4]
print(newList)

name = ["Sukhdeep", "Kunal", "Dev", "Mehta", "Panesar"]
newList = [item for item in name if "u" in item]
print(newList)

