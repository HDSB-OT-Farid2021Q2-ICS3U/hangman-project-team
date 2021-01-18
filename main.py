# TODO: computer picks word (from word list) that is going to be guessed

import random
import wordlist # list of possible words

x = random.randint(0, len(wordlist.wordlist)-1) # position of random word in word list

word=wordlist.wordlist.pop(x) # random word



#TODO check w/others

letter=input('Enter a letter guess:')

def blanks(word):
    '''prints the blanks of the word'''
    blanks = [x if x == letter.lower() else "_" for x in word] 
    print(" ".join(blanks))

def guessing(word):
    '''user is going to guess the word, checks if it's right'''
    guess = input("Enter your guess: ")
    if guess.lower() == word:
        print("Yay you guessed it!")
    else:
        print("Oops, try again")

#TODO make the hangman so it'll draw another part if wrong

.