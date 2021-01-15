# word list 

import random
import wordlist # list of possible words

x = random.randint(0, len(wordlist.wordlist)-1) # position of random word in word list

word=wordlist.wordlist.pop(x) # random word

print(word) 