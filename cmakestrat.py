import sys
import re
import os
import random

"""
The goal is to have a collection of codemaking strategy functions defined here.  They will all
take the same arguments as one another so that they can easily be swapped for one another in 
the mastermind.py program.  The Mastermind.py file will reference a strategy here as it runs the game.  
"""

def cmakestratHelper(name, param1, param2, param3):  #there has to be a better way to do what I'm doing here but this works for now
  #name: name of the codemaking strategy method
  #param1: rounds  (perhaps there are sophisticated codemaking strategies that think about how long the game is-- need to have this built in)
  #param2: colors
  #param3: slots
  #params 1 - 3 are everything that a codemaking strategy needs to know in order to act
  if(name=="randomCode"):
    randomCode(rounds, colors, slots)
  elif(name=="askAHuman"):
    askAHuman(rounds, colors, slots)
  #more elifs if we want more codemaking strategies
  else:
    print("Codemaking strategy "+name+" doesn't exist")
    sys.exit(1)

def randomCode(rounds, colors, slots):
  code = ''
  i=0
  while i<slots:
    code = code + str(random.randrange(0,colors))
    i=i+1
  return code

def askAHuman(rounds, colors, slots):
  print("You are making a code for a mastermind game that has "+rounds+"rounds,"+colors+" colors, and "+slots+"slots")
  code = str(input("Enter your code:")) #assumes proper formatting
  return code