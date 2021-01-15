word = "apple"

#TODO check w/others

def blanks(word):
    '''checks if letter inputed is in the word'''
    letter = input("Enter a letter: ")
    blanks = [x if x == letter.lower() else "_" for x in word] 
    print(" ".join(blanks))

blanks(word)

#wow its beautiful