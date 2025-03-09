import os

# os.mkdir("data Exercise")
# while True:
#     for file in os.listdir('data/.'):
#
#             os.rename(f"data/{file}", f"data/{i}.png")
#         i += 1
#     break

print(os.listdir("data Exercise/"))
def change_number_of_file():
    i = 1
    a = input("Enter file extension: ")
    while True:
        for file in os.listdir("data Exercise/"):
            if a == ".png":
                if file.endswith('.png'):
                    os.rename(f"data Exercise/{file}", f"data Exercise/{i}.png")
                    i += 1
            elif a == ".pdf":
                if file.endswith('.pdf'):
                    os.rename(f"data Exercise/{file}", f"data Exercise/{i}.pdf")
                    i += 1
            elif a == ".txt":
                if file.endswith('.txt'):
                    os.rename(f"data Exercise/{file}", f"data Exercise/{i}.txt")
                    i += 1
            elif a == ".asm":
                if file.endswith('.asm'):
                    os.rename(f"data Exercise/{file}", f"data Exercise/{i}.asm")
                    i += 1
            else:
                print("file extension not recognized")
                break
        break

change_number_of_file()
