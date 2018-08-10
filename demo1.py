###########################################################################################################################
#                                                                                                                         #  
#                                                                                                                         #
#                                                       DAY -1                                                            #
#                                                                                                                         #
#                                                                                                                         # 
###########################################################################################################################


#PRINT THE HELLO WORLD WITH THE HELP OF PRINT FUNCTION

print("Hello World")

#PRINT A 'NAME' VARIABLE WHICH CONTAINS A VARIABLE NAME ALSO

name = "Devraj"
print(name)
name =15

# ADD,SUB,MUL,DIV,PERCN,SQRT,MOD
print("5 + 2 =",5+2)
print("5 - 2 =",5-2)
print("5 * 2 =",5*2)
print("5 / 2 =",5/2)
print("5 % 2 =",5%2)
print("5 ** 2 =",5**2)
print("5 // 2 =",5//2)

#EXPERIENCE WITH ARITHMETIC 
print("1 + 2 - 3 * 2", 1 + 2 - 3 * 2)
print("(1 + 2 - 3) * 2",(1 + 2 - 3) * 2)

#STRING & MULTI_LINE_STRING

quote = "human stupidity & the universe"
multi_line_quote = "i am not sure about the universe"
print("%s %s %s" %("Two things are infinite !",quote,multi_line_quote))

#DATA_LIST  / DATA_STRUCTURE / MULTIPLE_CLASS
#CREATE A DATA LIST SET

grocery_lists =['juice','Tomatoes','Potatoes','Bannas']
print(grocery_lists[0])
print('First Item',grocery_lists[0])
grocery_lists[0]='Ice Cream'
print('First Item',grocery_lists[0])
print("\n Print the grocery_list \n")
print(grocery_lists)
other_events =['Wash Car','Pick up Kids','Cash Check']
print("\n Print the other_events \n")
print(other_events)

#CREATE A MASTER DATA SET

to_do_lists=[other_events,grocery_lists]
print(to_do_lists)
print(to_do_lists[1][1])

#APPEND FUNCTION TEST

grocery_lists.append("Apple")
grocery_lists.append("Mango")
print(to_do_lists)
print(grocery_lists)

#INSERT FUNCTION TEST
grocery_lists.insert(1,"Orange")
grocery_lists.insert(2,"Milk")
grocery_lists.insert(3,"Butter")
grocery_lists.insert(4,"Dahi")
print(grocery_lists)

#SORTED DATA LIST ELEMENTS

grocery_lists.sort()
print('sorted_list',grocery_lists)

#REVERSE DATA LIST ELEMENTS

grocery_lists.reverse()
other_events.reverse()
print(to_do_lists)

#LEGTH , MAXIMUM  & MINIMUM 
to_do_lists2 = grocery_lists + other_events
print(len(to_do_lists))
print(max(to_do_lists))
print(min(to_do_lists))


###########################################################################################################################
#                                                                                                                         #  
#                                                                                                                         #
#                                                       DAY -2                                                            #
#                                                                                                                         #
#                                                                                                                         # 
###########################################################################################################################

#IMPORT SYS , OS ,RANDOM 
import random
import sys
import os

# DICT_VALUES_KEY
super_footballer = {'Golden Boot' : 'Zidane','Golden Glove':'Buffon','Golden Player':'Ronaldhinho','Golden Ball':'Ronaldo'}

# GET keys 
print(super_footballer.get('Golden Boot'))
print(super_footballer.get('Golden Glove'))
print(super_footballer.get('Golden Player'))
print(super_footballer.get('Golden Ball'))

#GET VALUES & KEYS
print(super_footballer.keys())
print(super_footballer.values())

#PRINT KEYS

print(super_footballer['Golden Ball'])
print(super_footballer['Golden Boot'])
print(super_footballer['Golden Player'])
print(super_footballer['Golden Glove'])

#INSERT NEW KEYS
super_footballer['Golden Goal'] = 'Germany'
print(super_footballer.keys())
print(super_footballer.values())

#ALTER NEW VALUES
super_footballer['Golden Goal'] = 'England'
print(super_footballer.keys())
print(super_footballer.values())

#REMOVE KEYS_VALUES FROM DICT_LIST

del super_footballer['Golden Goal']
print(super_footballer.keys())
print(super_footballer.values())

#IMPORT RANDOM , SYS , OS

import random
import sys
import os

#####################################################    LOOPING     ##########################################################
# IF-ELIF-ELSE CONDITION
#PROGRAM AGE , ALREADY VOTER ,VOTER , UNDER AGED IDENTIFICATION
#IMPORT RANDOM , SYS , OS

import random
import sys
import os

# IF-ELIF-ELSE
age = 30

if age > 18:
    print("You are already a Voter")
elif age == 18:
    print("You are eligible as a voter")
else:
    print("You are under Age")
if (age >= 1) and (age <= 18):
    print("You have a birthday!")
elif ( age >= 18 ) or ( age <= 65):
   print("You have a birthday !")
#elif not(age == 30):
#    print("You don't get a birthday")
else:
    print(" Oh Yeah ! You have a birthday ")
    
###########################################################################################################################
#                                                                                                                         #  
#                                                                                                                         #
#                                                       DAY -3                                                            #
#                                                                                                                         #
#                                                                                                                         # 
###########################################################################################################################

#PRINT THE X VALUES '0' TO '9' USING FOR LOOP
for x in range(0,10):
    print(x,'',end="")
    print('\n')
    
grocery_lists =['juice','Tomatoes','Potatoes','Bannas']
for y in grocery_lists:
    print(y)

for x in [2,4,6,8,10]:
    print(x)

num_list = [[1,2,3],[10,20,30],[100,200,300]]
    
for x in range (0,3):
        for y in range(0,3):
            print(num_list[x][y])


    























