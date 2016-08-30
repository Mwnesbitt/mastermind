import sys
import re
import os
import random

"""
The goal is to have a collection of strategy functions defined here.  Then the Mastermind.py file
can work in such a way where the logic selects a strategy to use.  It's possible that you may
want to structure things such that "user choosing" is a strategy that's part of this set
"""

def randomguess():
  code = ''
  i=0
  while i<4:
    code = code + str(random.randrange(0,6))
    i=i+1
  return code
  
def dontbedumb():
### checks the guess against all previous guesses and grades it and throws it out if the grades aren't all equal
  return ""