word = "apple"

#TODO check w/others

def blanks(word):
    '''prints the blanks of the word'''
    blanks = [x if x == letter.lower() else "_" for x in word] 
    print(" ".join(blanks))

blanks(word)

def guessing(word):
    '''user is going to guess the word, checks if it's right'''
    guess = input("Enter your guess: ")
    if guess.lower() == word:
        print("Yay you guessed it!")
    else:
        print("Oops, try again")

#TODO make the hangman so it'll draw another part if wrong

#wow its beautiful