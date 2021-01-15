# word list 

import random
import wordlist

x = random.randint(0, len(wordlist.wordlist)-1)


print(wordlist.wordlist.pop(x))