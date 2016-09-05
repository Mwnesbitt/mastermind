import sys
import mastermind
import csv
"""
This file is a wrapper that runs mastermind.py many times to record output and do analysis on strategies.  The two main KPIs for 
evaluating the performance of a strategy is avg number of guesses req'd to break the code and avg runtime.
"""

def multipleColorsSlots(rounds, startColors, endColors, startSlots, endSlots, codemakestrategy, codebreakstrategy, iterations):
    
    colorsList=[]
    slotsList=[]
    guessesPerList=[]
    slots=int(startSlots)
    while slots<=int(endSlots):
        colors=int(startColors)
        while colors<=int(endColors):
            guessesPer=runGameMultiple(rounds, colors, slots, codemakestrategy, codebreakstrategy, iterations)             
            #print ("Colors: "+str(colors))
            #print ("Slots: "+str(slots))
            #print ("Guesses per Game: "+str(guessesPer))
            colorsList.append(colors)
            slotsList.append(slots)
            guessesPerList.append(guessesPer)
            colors=colors+1
        slots=slots+1
    rows = zip(colorsList,slotsList,guessesPerList)
    with open('output.csv', 'w',encoding='utf8',newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)    
        header=['Iterations :'+iterations]
        writer.writerow(header)
        header=["Code make: "+codemakestrategy]
        writer.writerow(header)
        header=["Code break: "+codebreakstrategy]
        writer.writerow(header)
        header=['Colors', 'Slots', 'Guesses Per Game']
        writer.writerow(header)
        for item in rows:
            writer.writerow(item)
        csvfile.close()
        
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
    return guessesPer

def main():
    if (len(sys.argv) != 9):
        print("pre-screen")
        print("Here are the params required to run this program:")
        print("wrapper.py rounds startColors endColors startSlots endSlots cmakestrat cbreakstrat iterations")
        for item in sys.argv:
            print(item)
        sys.exit(0)  
  #try:
    multipleColorsSlots(sys.argv[1],sys.argv[2],sys.argv[3],sys.argv[4],sys.argv[5],sys.argv[6],sys.argv[7],sys.argv[8])
  
    #outcome=runGameMultiple(sys.argv[1],sys.argv[3],sys.argv[5],sys.argv[6],sys.argv[7],sys.argv[8])
    #guessesPer=outcome
    #print ("Guesses Per Game: "+str(guessesPer))
    
if __name__ == '__main__':
  main()
        
