###########################################################################################################################
#                                                                                                                         #  
#                                                                                                                         #
#                                                   TUTORIAL - 1                                                          #
#                                                                                                                         #
#                                                                                                                         # 
###########################################################################################################################


#IMPORT RANDOM , SYS , OS

import random
import sys
import os
#import math
from math import sqrt
# TUTORIAL 1
# VARIABLE TYPE 

integerEx = 5
longintEx = 1000000000000000000000
floatEx = 3.1
stringEx = " Welcome to Python "
booleanEx1 = True

# FUNCTION CALLING TYPE () #

print (type(integerEx))
print (type(longintEx))
print (type(floatEx))
print (type(stringEx))
print (type(booleanEx1))

booleanEx2 = False

print ((booleanEx1) and (booleanEx2))
print ((booleanEx1) or (booleanEx2))
print (not (booleanEx2))



intOne = 7
intTwo = 99
floatOne = 7.9
floatTwo = 9.8

sum = intOne + intTwo

print('\n')
print("sum :",sum)
print('\n')

print( intTwo /intOne )
print( float(intTwo)/float(intOne))
print(int(floatOne))
print(floatOne // floatTwo)
print(int(booleanEx1))

print(intOne == intTwo)
print(intOne >= intTwo)
print(intOne <= intTwo)
print(intOne != intTwo)
print(intOne + intTwo)
print(intOne - intTwo)
print(intOne * intTwo)
print(intOne ** intTwo)
print(intOne  / intTwo)
print(intOne // intTwo)
print(intOne % intTwo)

print(sqrt(intOne))

#LONG STRING

longstr = "If you want to live a happy life, tie it to a goal, not to people or things"
print(longstr)

#RAW INPUT

raw_input=input()
print("what's your name ? ")
print("Hello , " + raw_input)

#ANOTHER STRING , USE "" ,' ',INPUT
raw_input=input()
print("what's your name ? ")
print("Hello , " + raw_input)
longstr = "If you want to live a happy life, tie it to a goal, not to people or things"
print(longstr)
anotherstr = 'Hi ,"Whats going on"'
print(anotherstr)
