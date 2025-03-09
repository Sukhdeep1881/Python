# Custom error are used when we want to stop our program at one point because sometime other going wrong if program run
# also helps in find certain line where error occurred if error occurred by specific line
a = (int(input("Enter any value between 5 and 9: ")))
if a < 5 or a > 9:
    raise ValueError("Value should be between 5 and 9") # using raise keyword to raise custom errors

salary = int(input("Enter salary amount: "))
if not 2000 < salary < 5000:
    raise  ValueError("Not data Exercise valid salary")

a = (input("Enter any value between 5 and 9 or quit: "))
if a == "quit" or a == "Quit":
    print("Goodbye")
elif int(a) < 5 or int(a) > 9:
    raise ValueError("Value should be between 5 and 9")

class CustomError(Exception):
    print("Custom Error") # this is used to write our own error like specific think we want like specific words etc

a = int(input("Enter any value between 5 and 9 or quit: "))
if a < 5 or a > 9:
    raise CustomError("Custom Error")
