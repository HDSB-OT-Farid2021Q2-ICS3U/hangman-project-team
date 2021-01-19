#Code: The code selects a word from the list, and the player is supposed to guess the word, either as a whole or each individual letter.
#authors: Zoey Xie, Milton Wang, Nicole Pinto
#filename: main.py
#date: 1-19-2021
#program: allows the player to play a game of hangman and guess a word selected by the computer
#revision: 1-19-2021

#asking so we know which clear to use
import os 

system = input("Do you use cls or clear? ")
if system.lower() == "cls":
    cls = lambda: os.system('cls')
elif system.lower() == "clear":
    clear = lambda: os.system('clear')
else:
    cls = lambda: os.system('cls')   

#essentially just the clear() or cls() 
def clearing(system):
    '''clears the terminal'''
    if system == "clear":
        clear()
    else:
        cls()

#computer picks word (from word list) that is going to be guessed
import random
import wordlist # list of possible words

#chooses the random word the user must guess
def randomword():
    '''chooses a random word that user will guess'''
    x = random.randint(0, len(wordlist.wordlist)-1) # position of random word in word list
    word = wordlist.wordlist.pop(x) # random word
    game(word)

# function that prints the "_" by checking if letter is in word
def blanks(word, letter, blank):
    '''checks if letter is in the word or not, replaces them with "_"'''
    for x in range(0, len(word)):
        if word[x] == letter.lower():
            blank[x] = letter
        elif blank[x] != "_":
            continue
        else:
            blank[x] = "_"
    print(" ".join(blank))

#main game function
def game(word):
    '''main game function: checks for wrong guesses, asks for guesses'''
    print("~Hangman!~")
    blank = [x if x == " " else "_" for x in word]  #variable that holds all the "_"
    print(" ".join(blank))
    wrongguesses = 0
    listofletters = []
    
    while wrongguesses < 10:
        which = input("Would you like to guess a letter or the word? ") #asks the user which they want to guess
        
        if which.lower() == "letter":
            letter = input("Enter a letter: ")
            if letter in listofletters:
                print("You already guessed this letter!")
                continue
            else:
                listofletters.append(letter)
            if letter.lower() in word:
                blanks(word, letter, blank)
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
                
    if wrongguesses >= 10:
        print(":p sorry you didn't win")
    
    end()


#Final Question to continue the game
def end():
  done = input('Are you done playing the game?(yes or no) ') #asks the user if they still want to play or not
  if done == 'yes':
    print('Thank you for playing!')
    clearing(system)
  elif done == "no":
    clearing(system)
    randomword()



randomword()
