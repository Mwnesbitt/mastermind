import sys
import cbreakstrat
import cmakestrat
import helperfunctions
  
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
  """
  ^^^There has to be a better way than using the helper methods I made, but they work for now.  
  Something like: cmakestrat.codemakestrategy(rounds, colors, slots)
  
  Below: Now we start looping through the rounds-- this process builds up the history object
  after every guess from a cbreakstrat method, and then hands the new history back to 
  that method to make another guess on.  runGame and whatever cbreakstrat method was 
  selected pass the action back and forth until the game is over.  
  """
  while rounds>0:
    guess=cbreakstrat.cbreakstratHelper(codebreakstrategy,rounds, colors, slots, history) #check your indexing on what the strats are expecting-- round n or n-1?
    roundgrade=helperfunctions.gradeguess(colors, slots, code, guess) 
    temp=[]
    temp.append(guess)
    temp.append(roundgrade)
    history.append(temp)
    print("round "+str(len(history)))
    for item in history:
      print(item)
    rounds = rounds-1
    if(roundgrade[0]==slots):
      return ("broken",code,len(history))
    if(rounds==0):
      return ("unbroken",code,len(history))

def main():  #now that the wrapper is built, we may not need a main method.  We're not deleting anything just yet, but consider streamlining.
  #main method assumes that setting up a game, the user will define a 5-tuple: 
  #number of rounds, number of colors, number of slots, codemaking strategy, codebreaking strategy
  
  if (len(sys.argv) != 6):
    print("pre-screen")
    print("Here are the params required to run this program:")
    print("mastermind.py rounds colors slots cmakestrat cbreakstrat")
    for item in sys.argv:
      print(item)
    sys.exit(0)  
  #try:
  outcome=runGame(sys.argv[1],sys.argv[2],sys.argv[3],sys.argv[4],sys.argv[5])
  if(outcome[0]=="broken"):
      print("Code Broken!")
      print("Code was: "+outcome[1]+". It took you "+str(outcome[2])+" guesses to get this.")
  elif(outcome[0]=="unbroken"):
      print("That was the last round!")
      print("Code not broken.  Code was: "+outcome[1]+". It took you "+str(outcome[2])+" guesses to get this.")
  else:
      print("An error has occurred")
  """
  except:
    print("Exception catch")
    print("Here are the params required to run this program:")
    print("python mastermind.py rounds colors slots cmakestrat cbreakstrat")
    for item in sys.argv:
      print(item)
    sys.exit(0)
  """

# This is the standard boilerplate that calls the main() function.
if __name__ == '__main__':
  main()