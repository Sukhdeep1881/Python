# if __name__ == "__main__": is used to stop printing every function
# because importing bring everything to stop this use this

def welcome():
    print("Hey you are welcome from Sukhdeep")

def welcome_back():
    print("Hey you are welcome from Sukhdeep")

# welcome() # runs in main class without calling

# runs only if call otherwise not
if __name__ == "__main__": # this function allows this only run one time here
    # run in main class if it is call only
    welcome_back()

print(__name__) #  gives main because it runs in main class
# on other files it give its own file name
