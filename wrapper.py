import sys
import re
import os
import random
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