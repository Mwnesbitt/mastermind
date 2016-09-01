import sys
import re
import os
import random
"""
Functions that other .py files need to be able to reference.  .py files cant import one another.
"""

def dontBeDumbBaseN(num,b,numerals="0123456789abcdefghijklmnopqrstuvwxyz"):
    return ((num == 0) and numerals[0]) or (dontBeDumbBaseN(num // b, b, numerals).lstrip(numerals[0]) + numerals[num % b])

def dontBeDumbIncrementGuess(guess, colors):
  temp=int(guess, colors)
  temp = temp+1
  temp = dontBeDumbBaseN(temp,colors)
  shortguess = str(temp)
  i=len(shortguess)
  while i<len(guess):
    shortguess="0"+shortguess
    i=i+1
  return shortguess
  
def gradeguess(colors, slots, code, guess):
  #assumes properly formatted code and guess--strings of 0 to colors with length slots
  blackpegs=0
  whitepegs=0
  i=0
  #print(guess)
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

  
def isWellFormed(string, colors, slots):
  #assumes string is a bunch of numbers
  if(len(string)!=slots):
    return False
  i=0
  while i<len(string):
    if(int(string[i])<0):
      return False
    if(int(string[i])>slots-1):
      return False
  return True