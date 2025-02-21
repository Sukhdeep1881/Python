# snake --> snake 0 water 1 Gun -1
# water --> snake -1 water 0 Gun 1
# Gun --> Snake 1 water -1 Gun 0
import random
print("Lets play Snake, water and Gun!!!!!!")
score = 0
scorePc = 0

while True:
    c = int(input("Choose 0 for Snake, 1 for Water or 2 for Gun: "))
    if c == 0:
        print("User chose Snake")
        b = random.randint(0, 2)
        if b == 0:
            print("Pc chose Snake")
        if b == 1:
            print("Pc chose Water")
            score +=1
        if b == 2:
            print("Pc chose Gun")
            scorePc +=1
    elif c == 1:
        print("User chose Water")
        b = (random.randint(0, 2))
        if b == 0:
            print("Pc chose Snake")
            scorePc += 1
        if b == 1:
            print("Pc chose Water")
        if b == 2:
            print("Pc chose Gun")
            score +=1
    elif c == 2:
        print("User chose Gun")
        b = (random.randint(0, 2))
        if b == 0:
            print("Pc chose Snake")
            score += 1
        if b == 1:
            print("Pc chose Water")
            scorePc += 1
        if b == 2:
            print("Pc chose Gun")
    print("Your score is:", score)
    print("Pc score is:", scorePc)
    if score == 3:
        print("You won the game!")
        break
    if scorePc == 3:
        print("You lose the game!")
        break




