import time
from time import localtime
a = (time.strftime("%H %M%S"))
print(a)

if a == time.strftime("00:00:00"):
    print("midnight")

if time.strftime("00:00:00") < a <= time.strftime("06:00:00"):
    print("Good sleep time")

elif time.strftime("07:00:00") <= a < time.strftime("12:00:00"):
    print("Good morning")

elif a == time.strftime("12:00:00"):
    print("noon")

elif time.strftime("12:00:00") < a <= time.strftime("16:00:00"):
    print("Good afternoon")

elif time.strftime("16:00:00") < a <= time.strftime("21:00:00"):
    print("Good evening")

elif time.strftime("21:00:00") < a <= time.strftime("23:59:59"):
    print("Good night")

print(localtime(40000000))
print(time.strftime("%H:%M:%S", localtime()))
a = int(time.strftime("%H", localtime()))
print(type(a))