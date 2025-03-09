import time  # time module works with time-related operation, such as timekeeping, formatting, and the time conversion

# timekeeping --> the process of recording how long something takes
# formatting --> how time will display to user
# time conversion --> converting one unit of time to other like hours convert to minute etc.
def using_while():
    i = 0
    while i < 50000:
        i = i + 1
        print(i)


def using_for():
    for i in range(50000):
        print(i)

init = time.time() # returns the current time as a floating-point number since the epoch means 1 Jan 1970
using_for()
t1 = time.time() - init
using_while()
print(t1) # time keeping
print(time.time() - init)  # time keeping

print(time.time())

print(4)
time.sleep(3) # wait for 3 second to print next line
print("This is printed after 3 seconds")

print("Start:", time.time())
time.sleep(3)
print("End:", time.time())

# to print the time in specific format
t = time.localtime()
formatted_line = time.strftime("%Y-%m-%d %H:%M:%S", t)
print(formatted_line)
print(time.asctime(time.localtime())) # direct way to print time and date