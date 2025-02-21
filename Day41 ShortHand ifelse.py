# In shorthand if else we have to write print statement first then if condition followed by else ""
# use only in short things using it in long logic condition cause difficulty in readability
a = 330
b = 3303
print("A") if a > b else print("=") if a == b else print("B")

print(9) if a > b else "" # else empty is required

c = 9 if a > b else 0
print(c)