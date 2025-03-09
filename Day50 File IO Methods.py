f = open("Day50MyFile.txt", "r")
while True:
    line = f.readline()  # readline used for reading line by line
    if not line: # when line empty break it
        break
    print(line)

while True:
    line = f.readline()
    print(line)
    if not line:
        print(line, type(line)) # line type is always string
        break

i = 0
while True:
    i = i + 1
    line = f.readline()
    if not line:
        break
    m1 = line.split(",")[0]
    m2 = line.split(",")[1]
    m3 = line.split(",")[2]
    print(f"Marks of student {i} in Maths is {m1*2}")  # all marks in string
    print(f"Marks of student {i} in English is {m2*2}")
    print(f"Marks of student {i} in SST is {m3*2}")
    print(line)

# type cast to int to use mathematical functions
j = 0
while True:
    j = j + 1
    line = f.readline()
    if not line:
        break
    m1 = int(line.split(",")[0])
    m2 = int(line.split(",")[1])
    m3 = int(line.split(",")[2])
    print(f"Marks of student {j} in Maths is {m1*2}")  # all marks in int
    print(f"Marks of student {j} in English is {m2*2}")
    print(f"Marks of student {j} in SST is {m3*2}")
    print(line)

# writelines methods used for writing data Exercise sequence of string to file.
file = open("Day50MyFile2.txt", "w")
lines = ['line 1\n', 'line 2\n', 'line 3\n']
file.writelines(lines)
file.close()

# if you have too many lines than use for loop with write method
file2 = open("Day50MyFile2.txt", "w")
lines = ['line 1', 'line 2', 'line 3']
for line in lines:
    file2.write(line+ '\n')
file2.close()


