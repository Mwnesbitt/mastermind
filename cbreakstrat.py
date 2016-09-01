import sys
import re
import os
import random

"""
The goal is to have a collection of codebreaking strategy functions defined here.  They will all
take the same arguments as one another.  Then the Mastermind.py file will reference a strategy here
as it runs the game.  
"""
def cbreakstratHelper(name, param1, param2, param3, param4):
  #name: name of the codebreaking strategy method
  #param1: rounds
  #param2: colors
  #param3: slots
  #param4: history
  #params 1 - 4 are everything that a codebreaking strategy needs to know about the state of the game in order to act
  if(name=="randomGuess"):
    randomGuess(param1, param2, param3, param4)
  elif(name=="askAHuman"):
    asAHuman(param1, param2, param3,param4)
  elif(name=="dontBeDumb"):
    dontBeDumb(param1, param2, param3, param4):
  #more elifs as we add more codebreaking strategies
  else:
    print("Strategy "+name+" doesn't exist")
    sys.exit(1)
    
def randomGuess(rounds, colors, slots, history):
  code = ''
  i=0
  while i<slots:
    code = code + str(random.randrange(0,colors))
    i=i+1
  return code
  
def askAHuman(rounds, colors, slots, history):
  print (code)
  history=[]
  while rounds>0:
    rounds = rounds-1
    guess = str(input("Take a guess: ")) #assumes a guess is properly formatted
    pegs=gradeguess(code,guess)
    temp=[]
    temp.append(guess)
    temp.append(pegs)
    history.append(temp)
    for var in history:
      print(var[0],var[1]) #assumes proper formatting-- might be fragile
    if(pegs[0]==4):
      print("You win!  The code was "+code)
      sys.exit(0)
    if(rounds==0):
      print("Sorry, you're out of guesses!  You lose!")
      print("The code was: "+code)
      sys.exit(0)
  
def dontBeDumb(rounds, colors, slots, history):
### cycles through all possible guesses, assuming each one is the actual code and checking to see
#if all previous guesses would grade to what they actually graded to.  Throws out the guess if not.
  return ""