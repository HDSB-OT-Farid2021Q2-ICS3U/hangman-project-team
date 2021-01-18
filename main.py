# word list 

import random
import wordlist # list of possible words

x = random.randint(0, len(wordlist.wordlist)-1) # position of random word in word list

word = wordlist.wordlist.pop(x) # random word

def blanks(word, letter, blank):
    where = word.find(letter)
    blank[where] = letter
    print(" ".join(blank))

def game(word):
    print("~Hangman!~")
    blank = [x if x == " " else "_" for x in word]
    print(" ".join(blank))
    guess = ""
    while guess != word:
        which = input("Would you like to guess a letter or the word? ")
        if which.lower() == "letter":
            letter = input("Enter a letter: ")
            if letter in word:
                blanks(word, letter, blank)
            else:
                print(" ".join(blank))
        elif which.lower() == "word":
            guess = input("Enter your guess: ")
            if guess.lower() == word:
                print("Yay you guessed it!")
                break
            else:
                print("Oops, try again")

game(word)


