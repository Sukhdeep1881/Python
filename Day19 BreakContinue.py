for i in range(12):
    print("5 *",i,"=",5*i)
    if i == 10:
        break # Use to break something like Loop e.g. if we want to break loop of 12 at 10


print("Skip the remaining Loop. Loop ko chodkar nikal gaya")

for k in range(13):
    if k ==10: # Check first then print not like above
        break
    print("5 *",k+1,"=",5*(k+1))

for k in range(13):
    if k == 10:
        print("Skip the iteration!")
        continue # continue is use for to skip only iteration not all loop break skip
    print("5 *",k,"=",5*k)

for k in range(1,101,1):
    print(k, end=" ")
    if k == 50:
        break
    else:
        print("Mississippi")
print("Thank you")

for i in [2,3,4,6,8,0]:
    if i % 2 != 0:
        continue
    print(i)

i=0
while True:
    print(i)
    i= i + 1
    if i % 100 == 0:
        break