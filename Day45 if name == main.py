# if __name__ == "__main__": is used to stop printing every function
# because importing bring everything to stop this use this
# when any print statement is already mentioned in importing file it will automatically execute
# therefore we use if functionName == main so it does not execute only required function execute
# if we only run import Day45_Sukhdeep it will print all printed or executed function in file
import Day45_Sukhdeep
# Day45_Sukhdeep.welcome()# it runs two times one from here and other from second file
Day45_Sukhdeep.welcome_back()# it runs one time using if __name__ == "__main__"

# only for reference used in imported file to check otherwise it will print this file as main
# print(__name__) # returns from where it is imported like other file name, but here gives same name