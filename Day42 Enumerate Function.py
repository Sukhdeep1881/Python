marks = [12, 56, 32, 98, 12, 45, 1, 4]

i = 0

# for i in range(len(a)):
#     print(i+1,a[i])

for index,mark in enumerate(marks): # enumerate function is a short way to print index of list, tuple etc. with value
    print(index,mark)

for index,mark in enumerate(marks, start=1): # start is used to start imdex from custom value
    print(index,mark)
    if index == 3:
        print("Sukhdeep, awesome!")

for marks in marks: # this for loop for finding index is too much long
    print(i, marks)
    if i == 3:
        print("Sukhdeep, awesome!")
    i += 1