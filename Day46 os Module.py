# only for reference everything in Garbage folder
import os
# os.mkdir("data") # creates a data function

# this condition check first
if not os.path.exists("data"): # check this file already created or not
    os.mkdir("data") # if not then create it


for i in range(0,100):
    os.mkdir(f"data/Day{i+1}")

import os

for i in range(0,100): # with os.rename folder name change from src to dst
    os.rename(f"data/Day{i+1}", f"data/Tutorial {i+1}")
    # os.rename(f"data/Tutorial {i + 1}", f"data/Day {i + 1}") # rename it again just change existing src name and add chosen dst name

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