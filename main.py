#asking so we know which clear to use
import os 
system = input("Do you use cls or clear? ")
if system.lower() == "cls":
    cls = lambda: os.system('cls')
elif system.lower() == "clear":
    clear = lambda: os.system('clear')
else:
    cls = lambda: os.system('cls')   

def clearing(system):
    if system == "clear":
        clear()
    else:
        cls()

#computer picks word (from word list) that is going to be guessed
import random
import wordlist # list of possible words

def randomword():
    x = random.randint(0, len(wordlist.wordlist)-1) # position of random word in word list
    word = wordlist.wordlist.pop(x) # random word
    game(word)

# function that prints the "_"
def blanks(word, letter):
    # where = ["_" if x != letter.lower() else letter for x in word]
    where = [word.find(letter)]
    blank[where] = letter
    print(" ".join(where))
    
def game(word):
    print("~Hangman!~")
    blank = [x if x == " " else "_" for x in word]
    print(" ".join(blank))
    wrongguesses = 0
    while wrongguesses < 10:
        which = input("Would you like to guess a letter or the word? ")
        if which.lower() == "letter":
            letter = input("Enter a letter: ")
            if letter in word:
                blanks(word, letter)
            else:
                print(" ".join(blank))
                wrongguesses += 1
                print(f'You have {10-wrongguesses} wrong guesses left!')
        elif which.lower() == "word":
            guess = input("Enter your guess: ")
            if guess.lower() == word:
                print("Yay you guessed it!")
                break
            else:
                print("Oops, try again")
                wrongguesses += 1
    #Final Question to continue the game
    done = input('Are you done playing the game?(yes or no) ')
    if done == 'yes':
        print('Thank you for playing!')
        clearing(system)
    elif done == "no":
        clearing(system)
        randomword()
        game(word)

randomword()