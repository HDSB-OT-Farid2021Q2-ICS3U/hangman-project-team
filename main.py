#asking so we know which clear to use
import os 
system = input("Do you use Windows or Mac? ")
if system.lower() == "windows":
    cls = lambda: os.system('cls)
elif system.lower() == "mac":
    clear = lambda: os.system('clear')
else:
    cls = lambda: os.system('cls')   

#computer picks word (from word list) that is going to be guessed
import random
import wordlist # list of possible words

x = random.randint(0, len(wordlist.wordlist)-1) # position of random word in word list

word = wordlist.wordlist.pop(x) # random word

# function that prints the "_"
def blanks(word, letter, blank):
    where = word.find(letter)
    blank[where] = letter
    print(" ".join(blank))
    
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
                blanks(word, letter, blank)
            else:
                print(" ".join(blank))
                wrongguesses += 1
        elif which.lower() == "word":
            guess = input("Enter your guess: ")
            if guess.lower() == word:
                print("Yay you guessed it!")
                break
            else:
                print("Oops, try again")

game(word)
    
#Final Question to continue the game
done = input('Are you done playing the game?(yes or no)')
if done == 'yes':
    print('Thank you for playing!')
    if system == "mac":
        clear()
    else:
        cls()
elif done == "no":
    game()

