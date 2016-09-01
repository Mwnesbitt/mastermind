import sys
import re
import os
import random
import helperfunctions

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
    return randomGuess(param1, param2, param3, param4)
  elif(name=="askAHuman"):
    return askAHuman(param1, param2, param3,param4)
  elif(name=="dontBeDumb"):
    return dontBeDumb(param1, param2, param3, param4)
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
  print(guess)
  return guess
  
def askAHuman(rounds, colors, slots, history):
  print("You are trying to break a code for a mastermind game that has "+str(rounds)+" rounds,"+str(colors)+" colors, and "+str(slots)+" slots.  History below:")
  for item in history:
    print(item[0], item[1]) #assumes history object is properly formed
  guess = str(input("Enter your guess:")) #assumes proper formatting-- use mastermind.isWellFormed to check and reject if False
  return guess
  
def dontBeDumb(rounds, colors, slots, history):  #runtime on this can definitely be improved...
  i=0
  guess=''
  while i<slots:
    guess = guess+"0"
    i=i+1
  #we have our initial guess of 0*.  Now we test it:
  if(history==[]):
    print(guess)
    return guess
  i=0
  while i<colors**slots:
    goodguess=True
    for item in history: #Go through the history of the game:
      if(guess==item[0]): #If this guess shows up as a guess in the history, throw it out, increment, and loop again
        goodguess=False
        break
      if(helperfunctions.gradeguess(colors, slots, guess, item[0])!=item[1]):  #If this guess has any chance of being right, assuming its the code would preserve the grades of previous guesses.  If it does for all guesses, accept it
        goodguess=False
        break
    if(goodguess==True):
      print("approved guess")
      return guess  
    else:
      #guess = randomGuess(rounds, colors, slots, history)
      guess = helperfunctions.dontBeDumbIncrementGuess(guess,colors) #increments the guess by 1   
    i=i+1  #the if statement should be true at some point, if not there's a bug somewhere
    
##other functions can be an improvement on dontbedumb where you try to avoid guessing the same color.
##google mastermind strategies to add more strategies here.