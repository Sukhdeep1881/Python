# Strings are immutable

a = "!!!!Sukhdeep!! !!!! Sukhdeep"
print(len(a))
print(a)
print(a.upper())
print(a.lower())
print(a.title())
print(a.capitalize())
print(a.swapcase())
print(a.rstrip("!")) # remove the trailing element in the string
print(a.replace("Sukhdeep!","Rajvir@"))

print(a.split(" "))

blogHeading = "introduction tO The console!!!"
print(blogHeading.capitalize())

str1 = "Welcome to the console!!!"
print(len(str1))
print(len(str1.center(50)))
print(str1.center(50))

print(a.count("Sukhdeep"))

str1 = "Welcome to the console!!!"
print(str1.endswith("!!!"))
print(str1.endswith("to",4,10))

str1 = "He's name is Dan. He is a an honest man."
print(str1.find("is")) # return -1 if not found
print(str1.index("is")) # same as find but find return -1 if not found but index return exception to stop the program
# print(str1.index("isss"))

str1 = "WelcomeToTheConsole"
print(str1.isalnum()) # return alphanumerical values only even space not allowed

str1 = "Welcome00"
print(str1.isalpha()) # return True if A-Z and a-z

str1 = "hello world"
print(str1.islower())
print(str1.isupper())

str1 = "we wish you a merry christmas"
print(str1.isprintable()) # return false if any character is not shown in output like \n \t
str1 = "we wish you a merry christmas\n"
print(str1.isprintable())

str1 = "we wish you a merry christmas"
print(str1.isspace()) # return false it only need space in string
str1 = "    "
print(str1.isspace())

str1 = "world heath organisation" # return true only if all words starts with capital letter
print(str1.istitle())
str1 = "World Heath Organisation"
print(str1.istitle())

str1= "Python is a Interpreted Language"
print(str1.startswith("Python"))

print(str1.swapcase()) # return opposite of character casing like small change to large A = a or a = A

str1 = "He's name is Dan. He is a an honest man."
print(str1.title())