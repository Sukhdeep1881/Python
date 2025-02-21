a = input("Enter the number: ")
print(f"Multiplication table of {a} is: ")

try:
    for i in range(1,11):
        print(f"{int(a)} X {i} = {int(a) * i}")
except Exception as e: # also putting e is your choice # we can also some comment in print like sorry some error occurred
    print(e)

try:
    for i in range(1,11):
        print(f"{int(a)} X {i} = {int(a) * i}")
except:
    print("sorry some error occurred")  # we can also put like invalid input!

print("Some imp lines of code")
print("End of program")

# try except for input validation and list index error handling
try:
    num = int(input("Enter an integer: "))
except ValueError:
    print("Number entered is not an integer.")

try:
    num = int(input("Enter an integer: "))
    a = [6, 3]
    print(a[num])
except ValueError:
    print("Number entered is not an integer.")
except IndexError:
    print("Index error")