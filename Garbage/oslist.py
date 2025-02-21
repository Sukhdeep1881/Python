import os
folder = os.listdir("data") # this method os.listdir("folder name") are used get list of file inside provided folder
# also this method prints arbitrary order (random or by chance)
print(folder)

# for folder in folder:
#     print(folder)

# for folder in folder:
#     print(folder)
#     print(os.listdir(f"data/{folder}")) # print what is inside data folder

# folder = os.listdir("data/Tutorial 1") # for single value print
# print(folder)

print(os.getcwd()) # print current working directory

# caution all upper function directory also, apply changes there also to work efficiently
os.chdir("/user") # change current working directory
print(os.getcwd()) # new directory will print