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
  """ 
  This method works by always attempting to guess 0*, and counting up from there.  But before it makes the actual guess, it 
  checks to see whether it was a "dumb guess" on two condition: 1. was this guess tried before? and 2. does this guess make 
  sense given the history of guesses and grades in the game?.  If a potential guess passes that test, it's returned.

  The runtime on this method can definitely be improved, possibly in several ways.  One way to do it would be to resume guessing
  at whatever the last guess was.  If we've thrown out a bunch of guesses from 0* to the latest guess previously, we don't need 
  to cycle through them and check them again because we already know they're bad.  There may be other runtime improvements as well,
  but the point is not to make this a killer algorithm as its only supposed to implement the "dontbedumb" strategy-- being smart is 
  another algorithm.
  
  I attempted to do some things with this strategy like the above-- using random guesses, e.g., but it wound up breaking the algorithm
  because it would often run out of time in the while loop and return nothing to the runGame method, which breaks runGame.  Those attempts
  are still in the code but are commented out-- they could probably be removed because I want to limit the scope on this algorithm and it
  does its job.  It's only meant to be "not dumb," after all.
  
  Another issue is the dontBeDumbIncrementGuess function, which doesn't know how to roll over back to 0*.  That's not an issue for the 
  way the algorithm is currently implemented, since it starts at 0* every time so it'll always run across every possible guess.  But 
  beSmartIncrementGuess will have to be able to do roll over, I think.
  """
  guess=''
  #guess=randomGuess(rounds, colors, slots, history)
  #Initial guess is 0*.
  i=0
  while i<slots:
    guess = guess+"0"
    i=i+1
  
  i=0
  while i<colors**slots: #Now that we have an initial guess, we check the history to make sure it isn't dumb
    goodguess=True
    for item in history: #Go through the history of the game:
      if(guess==item[0]): #If our proposed guess shows up as a prior guess in the history, it's a dumb guess.  
        goodguess=False
        break #pretty sure this isn't necessary.  Slight runtime improvement?
      if(helperfunctions.gradeguess(colors, slots, guess, item[0])!=item[1]):  #If the grades of prior guesses don't match the grades those guesses would have received if our proposed guess were the code, then our proposed guess is a dumb guess.
        goodguess=False
        break #pretty sure this isn't necessary.  Slight runtime improvement?
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
     to be done intelligently.  But we don't want to start out with 0* as the first guess, e.g.
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