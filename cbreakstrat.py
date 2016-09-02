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

  
def beSmart(rounds, colors, slots, history):
  """
  dontBeDumb is very close to the algorithm I use when playing mastermind, but is not quite what I use.
  dontBeDumb divides all possible guesses into two sets-- "not dumb" and "dumb" and it doesn't distinguish among
  "not dumb" guesses, guessing the first one that it comes to.  The game goes on this way until there's only one 
  "not dumb" guess, the answer.  beSmart will distinguish between among the "not dumb" guesses in 2 ways:
  1. I think guesses that aren't all a single color provide more utility in the future when checking a potential
     guess against the history of the game.  Thus, beSmart needs to select its next guess in a way that deprioritizes
     guesses that have doubled colors, where possible.  Keep in mind there may be more slots than colors, so this has
     to be done intelligently
  2. When I play the game, I usually look at my last guess and try to find the "nearest" not dumb guess for it (that 
     doesn't have doubled colors, as stated in part 1.).  So beSmart should try to do that, rather than just starting 
     at the same value the way dontBeDumb starts at 0* every time.  This will also help runtime, I think, because dontBeDumb
     has a bad runtime since it has to constantly check guesses that it has thrown out in the past, since it always has an 
     initial guess of 0*.
  beSmart will still guess the first "not dumb" guess that it comes to, but I want to design the strategy such that the 
  "increment guess" helper function suggests higher priority "not dumb" guesses before lower priority ones.  Thus, 
  beSmartIncrementGuess will need to take in the history (or at least the last guess) to start looking for "nearest" guesses
  to that one, and it will also have to find a way to deprioritize guesses that double up on lots of colors.  This will be tricky
  to do in a way that doesn't devastate the runtime of the algorithm-- if it runs across a deprioritized guess it can't skip it 
  and come back to it-- it needs to store it in an array and then its last attempt will be to empty that array.
  """
  return
  
##google mastermind strategies or use your big brain to add more strategies here.