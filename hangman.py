# draw the hangman
wrongguesses==0

def hangman():
  

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
