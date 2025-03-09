a = int(input("Enter your age: "))
print("Your age is: ",a)

# conditional operators
# >,<, >=, <=, ==, !=
# print(data Exercise>18)
# print(data Exercise<=18)
# print(data Exercise==18)
# print(data Exercise!=18)

if a > 18:          # No brackets required like other in c
    print("You can drive") # the space is indented is required to show it comes with if condition
    print("Yes")
else:
    print("You can not drive")
    print("No")
print("Thank you")  # if we remove indent we are out of condition this will simply print

applePrice = 210
budget = 200
if applePrice <= budget:
    print("Hey Google, add 1 Kg Apples to the cart.")
else:
    print("Hey Google, do not add Apples to the cart.")

applePrice = 120
budget = 200
if budget - applePrice > 100:
    print("Hey Google, add 1 Kg Apples to the cart.")
elif budget - applePrice > 50:
    print("Its okay you can buy")
else:
    print("Hey Google, do not add Apples to the cart.")

num = int(input("Enter the value of num: "))
if num < 0 :
    print("Number is negative")
elif num == 999:
    print("Number is special")
elif num == 0:
    print("Number is zero")
else:
    print("Number is positive")

print("I am happy now")

num = 18
if num < 0:
    print("Number is negative")
elif num > 0:
    if num <= 10:
        print("Number is between 1-10")
    elif 10 < num <= 20:
        print("Number is between 10-20")
    else:
        print("Number is greater than 20")
else:
    print("Number is zero")