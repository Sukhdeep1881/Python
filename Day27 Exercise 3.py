from playsound import playsound

Questions = ["What is the capital of India?",
             "Which planet is known as the \"Red Planet\"?",
             "Who is the author of the Harry Potter book series?",
             "In which year did India win its first Cricket World Cup?",
             "Who invented the telephone?",
             "Which element has the chemical symbol 'O'?",
             "Which Indian classical dance form originated in Kerala?",
             "Who was the first woman to win data Exercise Nobel Prize?",
             "What is the largest desert in the world?",
             "Who was the first President of the United States of America?"]

options = [("Mumbai","Kolkata","New Delhi","Chennai"),
         ("Venus", "Mars", "Jupiter", "Saturn"),
         ("J.R.R Tolkien", "J.K. Rowling", "George R.R. Martin", "Enid Blyton"),
         ("1975","1983","1987","1996"),
         ("Alexander Graham Bell", "Thomas Edison", "Nikola Tesla", "Guglielmo Marconi"),
         ("Gold", "Oxygen", "Osmium","Oganesson"),
         ("Kathak","Bharatnatyam","Kathakali","Odissi"),
         ("Mother Teresa", "Marie Curie", "Rosalind Franklin", "Jane Goodall"),
         ("Sahara Desert","Gobi Desert", "Kalahari Desert", "Antarctic Desert"),
         ("Abraham Lincoln", "George Washington", "John Adams", "Thomas Jefferson")]

Answer = ["New Delhi","Mars","J.K. Rowling","1983","Alexander Graham Bell","Oxygen","Kathakali", "Marie Curie", "Antarctic Desert", "George Washington"]

Price = [1000,5000,10000,50000,100000,320000,640000,125000,10000000,70000000]

i = 0
totalPrize = 0
print("Let's begin Kaun Banega Corepati")

while i < len(Questions) :
    print("\nQuestion", i+1,"for ",u'\u20B9',Price[i],":\n",Questions[i])
    print(options[i])
    answer = input("Enter your answer or Quit: \n")
    if answer == "Quit" or answer == "quit":
        print("You did well!!!")
        print("Total Prize Money Won:",u'\u20B9', Price[i])
        break
    if answer == Answer[i]:
        print("Correct!!!")
    elif answer != Answer[i]:
        print("Incorrect answer!!!")
        print("You lost the game!!!")
        print("Total Prize Money Won:",u'\u20B9', totalPrize)
        break
    if answer == Answer[9]:
        print("Congratulations!!!")
        print("You Won the game!!!")
        print("Total Prize Money Won:", u'\u20B9', "70000000")
        playsound('A:/Python/7crore.mp3')
    i += 1


