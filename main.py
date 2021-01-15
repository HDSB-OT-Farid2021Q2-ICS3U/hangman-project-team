# hi
# hi
# TODO: enter question details here
# 
# date and time completed: yyyy-mm-dd hh:mm
import os 
clear = lambda: os.system('clear')

while True: 
  done = input('Are you done playing the game?(yes or no)')
  if done == 'yes':
    print('Thank you for playing!')
    clear
 elif done == "no":
    print(game)