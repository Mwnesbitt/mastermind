import sys
import re
import os
import random
import helperfunctions
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
    return randomCode(param1, param2, param3)
  elif(name=="askAHuman"):
    return askAHuman(param1, param2, param3)
  #more elifs if we want more codemaking strategies
  else:
    print("Codemaking strategy "+name+" doesn't exist")
    sys.exit(1)

def randomCode(rounds, colors, slots):
  return helperfunctions.randomSequence(rounds, colors, slots)

def askAHuman(rounds, colors, slots):
  print("You are making a code for a mastermind game that has "+str(rounds)+" rounds,"+str(colors)+" colors, and "+str(slots)+" slots")
  code = str(input("Enter your code:")) #assumes proper formatting-- use mastermind.isWellFormed to check and reject if False
  return code
  
def minimizedDuplicates(rounds, colors, slots):
  """
  This would be like randomCode, but it could test the theory that its better to have fewer duplicate colors in your code.
  """
  return