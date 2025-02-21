import os

for i in range(0,100): # with os.rename folder name change from src to dst
    os.rename(f"data/Day{i+1}", f"data/Tutorial {i+1}")
    # os.rename(f"data/Tutorial {i + 1}", f"data/Day {i + 1}") # rename it again just change existing src name and add chosen dst name

