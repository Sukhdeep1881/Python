# <class '_io.TextIOWrapper'> type tells us everything is done inside built-in IO module
with open("Day51MyFile.txt","w") as file:
    file.write("123456789etSukhdeep")

with open("Day51MyFile.txt","r") as f:
    print(type(f))
    f.seek(10) # Move to the given byte
    data = f.read(5)  # start reading file after moving with the limit of given byte in read()
    print(data)

with open("Day51MyFile.txt","r") as f:
    print(type(f))
    f.seek(10) # Move to the given byte

    print(f.tell()) # gives the specific location from where file starts reading its content

    data = f.read(5)  # start reading file after moving with the limit of given byte in read()
    print(data)

with open("Day51MyFile.txt","w") as f:
    f.write('Hello World3!')
    f.truncate(5) # gives the first 5 bytes of file it is used to limit the output to specific bytes

with open("Day51MyFile.txt","r") as f:
    print(f.read())
