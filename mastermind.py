import sys
import re
import os
import random
import cbreakstrat
import cmakestrat

def gradeguess(colors, slots, code, guess):
  #assumes properly formatted code and guess--strings of 0 to 5 with length 4
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
    k=0 #k=0
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
  
  
def codebreaker():
  rounds = 6
  guesshistory=[]
  code = createcode(6,4)
  #print(code)
  while rounds>0:
    rounds = rounds-1
    guess = str(input("Take a guess: ")) #assumes a guess is properly formatted
    #print(code)
    pegs=gradeguess(colors, slots, code, guess)
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
      print("The code was: "+code)
      sys.exit(0)
  
def codemaker():
  code = str(input("Enter your code:")) #assumes proper formatting
  #for now, this will just guess random codes to get that up and running
  # this code is basically the codebreak code-- you need a helper function that handles the task of actually running the game?
  """
  The way implementing strategies will have to work is that the program has to keep track of the state of the game-- that's the
  guesses and their grades.  I've implemented that elsewhere-- it's a list where the first item in the list is a list with two items:
  the guess and its grade.  (The grade itself is a list of 2 numbers).  That object has to be passed to a strategy function which then
  uses that information about the state of the game to choose its guess.  So all strategy functions take our custom object that contains
  100% of information about the state of the game and return a guess.  To use a strategy to play the game you have to call it after each
  round. 
  """
  rounds = 10
  guesshistory=[]
  print(code)
  while rounds>0:
    rounds = rounds-1
    #will need a try catch where we use runnerMethod to call a strategy method.  But how do you pass in parameters, like # of colors and length?
    guess = createcode(6,4) #strategies.randomguess
    pegs=gradeguess(code,guess)
    print(guess,pegs)
    if(pegs[0]==4):
      print("The computer guessed your code.  You lose!")
      print("The computer was using strategy: randomguess")
      sys.exit(0)
    if(rounds==0):
      print("The computer didn't guess your code!  You win!")
      print("The computer was using strategy: randomguess")
      sys.exit(0)
  
def runGame(rounds, colors, slots, codemakestrategy, codebreakstrategy):
  rounds=int(rounds)
  colors=int(colors)
  slots=int(slots)
  history=[]
  
  code = cmakestrat.cmakestratHelper(codemakestrategy, rounds, colors, slots)
  #There has to be a better way than using the helper methods I made, but they work for now.  Something like: cmakestrat.codemakestrategy(rounds, colors, slots)
  
  #now we start looping through the rounds-- this process needs to build up the history object and pass it back and forth to cbreakstrat.codebreakstrategy()
  while rounds>0:
    guess=cbreakstrat.cbreakstratHelper(codebreakstrategy,rounds, colors, slots, history)
    roundgrade=gradeguess(colors, slots, code,guess)
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
