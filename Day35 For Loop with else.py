# else execution means loop is not broke, the loop will be successfully finished the last value is processed
for i in range(5):
    print(i)
else:               # else executed when loop is finished
    print("Sorry no i")

for i in []:   # else executed because loop is empty
    print(i)
else:
    print("Sorry no i")

for i in range(6):  # in this case there is no else printed because break statement stop the loop within loop therefore it not goes to else
    print(i)
    if i == 4: # also when value is 5 which is 6 in real it will also not run, but when 6 which is 7 it runs
        break
else:
    print("Sorry no i")

i = 0
while i < 7:  # same with while
    print(i)
    i = i + 1
    if i == 4:
        break
# else:
#     print("Sorry no i")

for x in range(5):
    print(f"iteration no {x+1} in for loop") # first way with f string method
else:
    print("else block in loop")

print("Out of loop")

for x in range(5):
    print("iteration no {} in for loop".format(x+1)) # second way with string format method
else:
    print("else block in loop")

print("Out of loop")

