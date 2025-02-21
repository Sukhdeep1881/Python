# READING A FILE
f = open("Day49myfile.txt","r") # r mode for read a file
# f = open("Day49myfile.txt") # r mode is default it will also works
# print(f)
text = f.read()
print(text)
print(f.read()) # or you can directly type this
f.close()

# WRITING A FILE
f = open("Day49myfile.txt","w")
f.write("Hello, world!")
# f.close()

# APPENDING A FILE
# if we click run again and again same content will be added in the end of file
f = open("Day49myfile.txt","a")
f.write("Hello, world!")
f.close()

# used as data storage
# shortcut using with method it automatically closed the file
with open("Day49myfile.txt","a") as f:
    # print(f.read())
    # f.write("Hey I am inside with")
    f.write("Hey I am inside with")
