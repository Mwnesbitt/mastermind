import sys
import re
import os
import random
import strategies

#Comment added to make sure I know how to merge and commit.
#Comment added to make sure I know how to branch, then commit, then merge.
def createcode(colors, length):
  #colors is the number of colors available in the game as an integer
  #length is the number of colored pegs in the code
  code = ''
  i=0
  while i<length:
    code = code + str(random.randrange(0,colors))
    i=i+1
  return code

def gradeguess(code, guess):
  #this is currently incorrectly implemented-- check wikipedia article to get the finer details correct
  """
  If there are duplicate colours in the guess, they cannot all be awarded a key peg unless they correspond to the same number of duplicate colours in the hidden code. For example, if the hidden code is white-white-black-black and the player guesses white-white-white-black, the codemaker will award two colored key pegs for the two correct whites, nothing for the third white as there is not a third white in the code, and a colored key peg for the black. No indication is given of the fact that the code also includes a second black
  """
  #assumes properly formatted code and guess
  blackpegs=0
  whitepegs=0
  i=0
  while i<4:
    if(guess[i]==code[i]):
      blackpegs = blackpegs+1
    else:
      k=0 #k=0, k=i?
      while k<4:
        if(guess[i]==code[k]):
          whitepegs=whitepegs+1
          break
        k=k+1
    i=i+1
  result=[blackpegs,whitepegs]
  return result
  
  
def codebreaker():
  rounds = 6
  guesshistory=[]
  code = createcode(6,4)
  #print(code)
  while rounds>0:
    rounds = rounds-1
    guess = input("Take a guess: ") #assumes a guess is properly formatted
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
      sys.exit(0)
  
def codemaker():
  code = input("Enter your code:") #assumes proper formatting
  #for now, this will just guess random codes to get that up and running
  # this code is basically the codebreak code-- you need a helper function that handles the task of actually running the game
  rounds = 10
  guesshistory=[]
  print(code)
  while rounds>0:
    rounds = rounds-1
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
  if len(sys.argv) != 2:
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
