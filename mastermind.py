import sys
import re
import os
import random
import strategies

# Define a main() function that prints a little greeting.
def createcode():
  #print("Program started")
  code = ''
  i=0
  while i<4:
    code = code + str(random.randrange(0,6))
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
  code = createcode()
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
    guess = createcode() #strategies.randomguess
    pegs=gradeguess(code,guess)
    print(guess,pegs)
    if(pegs[0]==4):
      print("The computer guessed your code.  You lose!")
      sys.exit(0)
    if(rounds==0):
      print("The computer didn't guess your code!  You win!")
      sys.exit(0)
  
  

def main():
  #The goal with the commented out text is for the user to customize: codebreaker, codemaker, maybe # of rounds, maybe length of code, strategies employed by computer if codemaking, etc.
  """
  if len(sys.argv) != 2:
    print(sys.argv[1])
    print(sys.argv[2])
    sys.exit(1)
  """
  codebreaker()
  #codemaker()
  
  
# This is the standard boilerplate that calls the main() function.
if __name__ == '__main__':
  main()
