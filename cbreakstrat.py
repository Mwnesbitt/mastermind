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
  return guess
  
def askAHuman(rounds, colors, slots, history):
  print("You are trying to break a code for a mastermind game that has "+str(rounds)+" rounds,"+str(colors)+" colors, and "+str(slots)+" slots.  History below:")
  for item in history:
    print(item[0], item[1]) #assumes history object is properly formed
  guess = str(input("Enter your guess:")) #assumes proper formatting-- use mastermind.isWellFormed to check and reject if False
  return guess
  
def dontBeDumb(rounds, colors, slots, history):  #Pretty sure runtime on this can be improved.
  """ There are definitely some issues with this method if you use random guesses-- it doesn't loop forever, and incrementing
  to the next code seems broken.  My concern here is that starting at 0* is probably not optimal so these errors need to be worked out
  if its really going to be the best algo.  I think the area to work them out is in helperfunctions.dontBeDumbIncrementGuess.  That function
  doesn't know how to roll over back to 0*.  If it did that, we could pick an initial guess of 1234...n and then increment.  Beyond that, 
  there could be an even more complicated function that increments more intelligently by skipping guesses that have doubled colors and coming
  back to them-- I suspect this is better because the guess gives you more information if there aren't doubled colors.
  """
  #guess=randomGuess(rounds, colors, slots, history)
  i=0
  
  #Have the initial guess be 0*.  I think it's probably best for initial guess to actually be all different colors if possible.
  guess=''
  while i<slots:
    guess = guess+"0"
    i=i+1
  i=0
  
  while i<colors**slots: #Now that we have an initial guess, we check the history to make sure it isn't dumb
    goodguess=True
    for item in history: #Go through the history of the game:
      if(guess==item[0]): #If this guess shows up as a prior guess in the history, it's a dumb guess.  
        goodguess=False
        break
      if(helperfunctions.gradeguess(colors, slots, guess, item[0])!=item[1]):  #If this guess isn't dumb, then assuming its correct would should preserve the grades of previous guesses.
        goodguess=False
        break
    if(goodguess==True):
        return guess  
    else:
      #guess = randomGuess(rounds, colors, slots, history)
      guess = helperfunctions.dontBeDumbIncrementGuess(guess,colors) #This needs fixing: It was built on the assumption that it would always start at 0*, so it doesn't know how to loop around.  I think that's the problem, anyway 
    i=i+1 
  print("Never found a good guess-- WTF?")
    
##other functions can be an improvement on dontbedumb where you try to avoid guessing the same color.
##google mastermind strategies to add more strategies here.