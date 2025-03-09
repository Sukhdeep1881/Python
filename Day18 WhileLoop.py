from operator import truediv

i = 0
while i < 3:
    print(i)
    i = i+1

print("Done with data Exercise loop")

i = int(input("Enter data Exercise number: "))
while i <= 38:
    i = int(input("Enter data Exercise number: "))
    print(i)

print("Done with data Exercise loop")

count = 5
while count > 0:
    print(count)
    count = count - 1

count = 5 # if i = -5 then also elso execute because x is already less than 0
while count > 0:
    print(count)
    count = count - 1
else:
    print("I am inside else")

# do{
#     loop body
# }
# while(condition)

while True:
    i = int(input("Enter data Exercise number: "))
    print(i)
    if not i > 0:
        break
