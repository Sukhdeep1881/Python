# finally is used to close database connection if you have multiple except statements or to close connections
# try:
#     l = [1, 5, 6, 7]
#     i = int(input("Enter the index: "))
#     print(l[i])
# except IndexError:
#     print("Some error occurred")

# finally keyword is used to execute everytime weather the error occurs or not
# it mostly used iin functions because outside print value also print but not in function
def func1():
    try:
        k = [1, 5, 6, 7]
        j = int(input("Enter the index: "))
        print(k[j])
        return 1
    except IndexError:
        print("Some error occurred")
        return 0 # finally come first before return

    finally:  # this will always run
        print("I am always executed")
        # print("I am always executed") # if it runs alone without finally it will not print


x = func1()  # if we direct call the function like func() it will not print return value
print(x)