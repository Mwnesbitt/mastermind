import sys
import re
import os
import random
import cbreakstrat
import cmakestrat

def gradeguess(colors, slots, code, guess):
  #assumes properly formatted code and guess--strings of 0 to colors with length slots
  blackpegs=0
  whitepegs=0
  i=0
  tempCode = list(code)#turn code into a list
  tempGuess = list(guess)#turn guess into a list
  while i<slots:#run through the code to check for black pegs
    if(tempGuess[i]==tempCode[i]):
      blackpegs = blackpegs+1
      tempCode[i]='b'#replace the black pegs with a b so it wont be counted in the white peg section
      tempGuess[i]='b'#replace the black pegs with a b so it wont be counted in the white peg section
    i=i+1
  i=0 #reset i for new loop
  while i<slots:#run through the code to check for white pegs
    k=0
    while k<slots:
        if(tempGuess[i]=='b'): #makes sure that black pegs aren't counted as being white pegs
            break
        if(tempGuess[i]==tempCode[k]):
            whitepegs=whitepegs+1
            tempGuess[i]='w'
            tempCode[k]='w'
            break
        k=k+1
    i=i+1
  result=[blackpegs,whitepegs]
  #print("code= "+code)
  #print("guess= "+"".join(tempGuess))
  return result

def runGame(rounds, colors, slots, codemakestrategy, codebreakstrategy):
  rounds=int(rounds)
  colors=int(colors)
  slots=int(slots)
  history=[]
  """
  The way implementing a game works is that runGame keeps track of the state of the game with the "history" object.  The state of the 
  game is simply what guesses have been made and what were their grades.  That combined with # of total rounds, # of colors, and # of slots
  is all that a strategy has available to make a guess.  
  
  The history object is a list of the results of different rounds.  A particular round is a list with two items: the guess and its grade. 
  The guess is a string of digits, and the grade is a list of 2 numbers-- the black pegs and white pegs. 
  """
  code = cmakestrat.cmakestratHelper(codemakestrategy, rounds, colors, slots)
  #There has to be a better way than using the helper methods I made, but they work for now.  
  #Something like: cmakestrat.codemakestrategy(rounds, colors, slots)
  
  #now we start looping through the rounds-- this process builds up the history object
  #after every guess from a cbreakstrat method, and then hands the new history back to 
  #that method to make another guess on.  runGame and whatever cbreakstrat method was 
  #selected pass the action back and forth until the game is over.  
  while rounds>0:
    guess=cbreakstrat.cbreakstratHelper(codebreakstrategy,rounds, colors, slots, history)
    roundgrade=gradeguess(colors, slots, code, guess)
    temp=[]
    temp.append(guess)
    temp.append(roundgrade)
    history.append(temp)
    if(roundgrade[0]==slots):
      print("Code Broken!")
      sys.exit(0)
    if(rounds==0):
      print("That was the last round!")
      print("Code not broken.  Code was: "+code)
      sys.exit(0)

def main():
  #main method assumes that setting up a game, the user will define a 5-tuple: 
  #number of rounds, number of colors, number of slots, codemaking strategy, codebreaking strategy
  
  if (len(sys.argv) != 6):
    print("pre-screen")
    print("Here are the params required to run this program:")
    print("mastermind.py rounds colors slots cmakestrat cbreakstrat")
    for item in sys.argv:
      print(item)
    sys.exit(1)  
  try:
    runGame(sys.argv[1],sys.argv[2],sys.argv[3],sys.argv[4],sys.argv[5])
  except:
    print("Exception catch")
    print("Here are the params required to run this program:")
    print("python mastermind.py rounds colors slots cmakestrat cbreakstrat")
    for item in sys.argv:
      print(item)
    sys.exit(1)       

# This is the standard boilerplate that calls the main() function.
if __name__ == '__main__':
  main()