import os 
system = input("Do you use Windows or Mac? ")
if system.lower() == "windows":
    cls = lambda: os.system('cls)
elif system.lower() == "mac":
    clear = lambda: os.system('clear')
else:
    cls = lambda: os.system('cls)   

#computer picks word (from word list) that is going to be guessed
import random
import wordlist # list of possible words

x = random.randint(0, len(wordlist.wordlist)-1) # position of random word in word list

word = wordlist.wordlist.pop(x) # random word

def blanks(word, letter, blank):
    where = word.find(letter)
    blank[where] = letter
    print(" ".join(blank))

def hangman():
  letter = input('Enter a letter guess:')
  wrongguesses=0
  if letter not in word:
    wrongguesses+=1
  while wrongguesses<10:
    letter=input('Enter a letter guess:')
    
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
    
#Final Question to continue the game
while True: 
  done = input('Are you done playing the game?(yes or no)')
  if done == 'yes':
    print('Thank you for playing!')
    clear
  elif done == "no":
    game()

