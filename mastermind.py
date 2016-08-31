import sys
import re
import os
import random
import strategies

def createcode(colors, length):
  #colors is the number of colors available in the game as an integer
  #length is the number of colored pegs in the code
  code=""
  i=0
  while i<length:
    code = code + str(random.randrange(0,colors))#Have you done any research on how "good" python's RNG is?
    i=i+1
  return code

def gradeguess(code, guess):
  #assumes properly formatted code and guess--strings of 0 to 5 with length 4
  blackpegs=0
  whitepegs=0
  i=0
  tempCode = list(code)#turn code into a list
  tempGuess = list(guess)#turn guess into a list
  while i<4:#run through the code to check for black pegs
    if(tempGuess[i]==tempCode[i]):
      blackpegs = blackpegs+1
      tempCode[i]='b'#replace the black pegs with a b so it wont be counted in the white peg section
      tempGuess[i]='b'#replace the black pegs with a b so it wont be counted in the white peg section
    i=i+1
  i=0 #reset i for new loop
  while i<4:#run through the code to check for white pegs
    k=0 #k=0
    while k<4:
        if(tempGuess[i]=='b'): #makes sure that black pegs aren't counted as being white pegs
            break
        if(tempGuess[i]==tempCode[k]):
            whitepegs=whitepegs+1
            tempGuess[i]='w'
            tempCode[k]='w'
            break
        k=k+1
    i=i+1
  result=[blackpegs,whitepegs]
  #print("code= "+code)
  #print("guess= "+"".join(tempGuess))
  return result
  
  
def codebreaker():
  rounds = 6
  guesshistory=[]
  code = createcode(6,4)
  #print(code)
  while rounds>0:
    rounds = rounds-1
    guess = str(input("Take a guess: ")) #assumes a guess is properly formatted
    #print(code)
    pegs=gradeguess(code,guess)
    temp=[]
    temp.append(guess)
    temp.append(pegs)
    guesshistory.append(temp)
    for var in guesshistory:
      print(var[0],var[1]) #assumes proper formatting-- might be fragile
    if(pegs[0]==4):
      print("You win!  The code was "+code)
      sys.exit(0)
    if(rounds==0):
      print("Sorry, you're out of guesses!  You lose!")
      print("The code was: "+code)
      sys.exit(0)
  
def codemaker():
  code = str(input("Enter your code:")) #assumes proper formatting
  #for now, this will just guess random codes to get that up and running
  # this code is basically the codebreak code-- you need a helper function that handles the task of actually running the game?
  """
  The way implementing strategies will have to work is that the program has to keep track of the state of the game-- that's the
  guesses and their grades.  I've implemented that elsewhere-- it's a list where the first item in the list is a list with two items:
  the guess and its grade.  (The grade itself is a list of 2 numbers).  That object has to be passed to a strategy function which then
  uses that information about the state of the game to choose its guess.  So all strategy functions take our custom object that contains
  100% of information about the state of the game and return a guess.  To use a strategy to play the game you have to call it after each
  round. 
  """
  rounds = 10
  guesshistory=[]
  print(code)
  while rounds>0:
    rounds = rounds-1
    #will need a try catch where we use runnerMethod to call a strategy method.  But how do you pass in parameters, like # of colors and length?
    guess = createcode(6,4) #strategies.randomguess
    pegs=gradeguess(code,guess)
    print(guess,pegs)
    if(pegs[0]==4):
      print("The computer guessed your code.  You lose!")
      print("The computer was using strategy: randomguess")
      sys.exit(0)
    if(rounds==0):
      print("The computer didn't guess your code!  You win!")
      print("The computer was using strategy: randomguess")
      sys.exit(0)
  
  

def main():
  """
  Future Goal in customizing the program:
  Allow the user to customize the program in several ways:
  1. "Analytics mode" where there aren't a bunch of things printed to the screen--
    this is the mode to use when trying to analytics and have the computer play itself.
    You may want to generate a file that has the results-- this could be a csv
    or something that could easily be imported into a graphing program like Mathematica
  2. Change the parameters of the game: # of rounds, length of code, strategies employed
    by the computer when the user is codemaking, etc.
  """
  """ 
  codeType = input("Select 1 for codebreaker or 2 for codemaker: ")
  if codeType == 1:
      print("You have selected codebreaker")
      codebreaker()
  elif codeType == 2:
      print("You have selected codemaker")
      codemaker()
  else:
      print("You need to specify 'codemaker' or 'codebreaker'")
      sys.exit(1)
  """
  if (len(sys.argv) != 2):
    print("You need to specify 'codemaker' or 'codebreaker'")
    for item in sys.argv:
      print(item)
    sys.exit(1)
  if (sys.argv[1]=="codemaker"):
    codemaker()
  elif (sys.argv[1]=="codebreaker"):
    codebreaker()
  else:
    print("You must select 'codemaker' or 'codebreaker'")
    sys.exit(1)
    
  
# This is the standard boilerplate that calls the main() function.
if __name__ == '__main__':
  main()
