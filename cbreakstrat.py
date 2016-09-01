import sys
import re
import os
import random

"""
The goal is to have a collection of codebreaking strategy functions defined here.  They will all
take the same arguments as one another so that they can easily be swapped for one another in 
the mastermind.py program.  The Mastermind.py file will reference a strategy here as it runs the game.  
"""
def cbreakstratHelper(name, param1, param2, param3, param4): #there has to be a better way to do what I'm doing here but this works for now
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
    dontBeDumb(param1, param2, param3, param4)
  #more elifs as we add more codebreaking strategies
  else:
    print("Codebreaking strategy "+name+" doesn't exist")
    sys.exit(1)

def randomGuess(rounds, colors, slots, history):
  guess = ''
  i=0
  while i<slots:
    guess = guess + str(random.randrange(0,colors))
    i=i+1
  return guess
  
def askAHuman(rounds, colors, slots, history):
  print("You are trying to break a code for a mastermind game that has "+rounds+"rounds,"+colors+" colors, and "+slots+"slots.  History below:")
  for item in history:
    print(item[0], item[1]) #assumes history object is properly formed
  guess = str(input("Enter your guess:")) #assumes proper formatting
  
def dontBeDumb(rounds, colors, slots, history):
#cycles through all possible guesses, assuming each one is the actual code and checking to see
#if all previous guesses would grade to what they actually graded to.  Throws out the guess if not.
  return ""