import os
# os.mkdir("data") # creates a data function

# this condition check first
if not os.path.exists("data"): # check this file already created or not
    os.mkdir("data") # if not then create it


for i in range(0,100):
    os.mkdir(f"data/Day{i+1}")

