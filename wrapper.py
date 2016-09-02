import sys
import mastermind
"""
The goal here is have this file be a wrapper that runs mastermind.py many times to record output.
It will run a computer v computer strategy where wrapper.py asks the user what strategies should be
used for codemaking and codebreaking, and then do that 1000 times and record the outputs
of each round and provide statistics, like how long it took to guess the code on average, etc.
This will be tricky-- it would be nice if the wrapper calling mastermind.py didn't print anything 
to the terminal, but we'll have to see how that works.  Might have to add another parameter into 
runGame that is a boolean on whether things get printed or not.  

It would be nice to have this program generate a file that contains the results-- maybe a csv
or something that could easily be imported into a graphing program like mathematica.  That way
the wrapper could run 1000 games for all (x,y) in a certain range where x and y are colors and slots.
Maybe different strategies have different tail behaviour-- one might be better with lots of colors
and a few slots, where as a different one might work better with few colors but lots of slots.
"""
#note: may want to add a way to run a simulation that actually cycles through all codes, rather than 
#randomly generating them for each individual game.  This could be done by adding a codemaking strategy
#called askAnOracle and then use a function in the wrapper to increment through all possible codes.  The
#oracle function would probably only need to be dontBeDumbIncrementGuess so all we would have to do would
#be to add some command line params to wrapper to specify this, I think.


def runGameMultiple(rounds, colors, slots, codemakestrategy, codebreakstrategy, iterations):
    i = int(iterations)
    win=0
    loss=0
    guesses=0
    while i>0:
        outcome = mastermind.runGame(rounds, colors, slots, codemakestrategy, codebreakstrategy)
        if(outcome[0] == "broken"):
            win = win+1
            guesses=guesses+outcome[2]
        elif(outcome[0] == "unbroken"):
            loss = loss+1
            guesses=guesses+outcome[2]
        else:#catch if something funky happens
            print("An error occurred")
            sys.exit(1)
        i = i-1
    
    
    guessesPer=float(guesses)/float(iterations)
    return (win,loss,guessesPer)

def main():
    if (len(sys.argv) != 7):
        print("pre-screen")
        print("Here are the params required to run this program:")
        print("wrapper.py rounds colors slots cmakestrat cbreakstrat iterations")
        for item in sys.argv:
            print(item)
        sys.exit(0)  
  #try:
    outcome=runGameMultiple(sys.argv[1],sys.argv[2],sys.argv[3],sys.argv[4],sys.argv[5],sys.argv[6])
    win=outcome[0]
    loss=outcome[1]
    guessesPer=outcome[2]
    print ("Wins: "+str(win))
    print ("Losses: "+str(loss))
    print ("Guesses Per Game: "+str(guessesPer))
    print ("You won 1 in "+str(loss/win)+" games")
if __name__ == '__main__':
  main()
        