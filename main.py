import os 
clear = lambda: os.system('clear')

#Final Question to continue the game
while True: 
  done = input('Are you done playing the game?(yes or no)')
  if done == 'yes':
    print('Thank you for playing!')
    clear
  elif done == "no":
    game()

#computer picks word (from word list) that is going to be guessed
import random
import wordlist # list of possible words

x = random.randint(0, len(wordlist.wordlist)-1) # position of random word in word list

word=wordlist.wordlist.pop(x) # random word


letter=input('Enter a letter guess:')

def blanks(word):
    '''prints the blanks of the word'''
    blanks = [x if x == letter.lower() else "_" for x in word] 
    print(" ".join(blanks))

# below is for guessing the whole word (not individual letter)
def guessing(word):
    '''user is going to guess the word, checks if it's right'''
    guess = input("Enter your guess: ")
    if guess.lower() == word:
        print("Yay you guessed it!")
    else:
        print("Oops, try again")

#TODO make the hangman so it'll draw another part if wrong



def hangman():
  
  wrongguesses=0

  for x in word:
    if letter!=x:
      wrongguesses+=1

    if wrongguesses==1:
      print('O')
    elif wrongguesses==2:
      print('|')
    elif wrongguesses==3:
      print(chr(92))  
    elif wrongguesses==4:
      print('/')
    elif wrongguesses==5:
      print('/')
    elif wrongguesses==6:
      print(chr(92))
    elif wrongguesses>=7:
      break        
