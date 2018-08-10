###########################################################################################################################
#                                                                                                                         #  
#                                                                                                                         #
#                                                   TUTORIAL - 3                                                          #
#                                                                                                                         #
#                                                                                                                         # 
###########################################################################################################################
#Dictonary : keys and values ... item() ,values()

#Create a Dictonary

dictEx = ({"Age":35,"Height":"6'3","Weight":56})
print(dictEx)
print('\n')

#Get function
print('\n')

print(dictEx.get("Age"))

#display items() 
print('\n')

print(dictEx.items())

#display values() 
print('\n')
print(dictEx.values())

#GET  KEYS
print('\n')
dictEx.keys()

#POP 
print('\n')
dictEx.pop("Age")
print(dictEx)


#PROGRAM 

strName = 'Louis'
floatAge = 32.7
charSex = 'M'
intChild = 2
boolMarried =True

print('Name    :',strName + '\n',' Age   : ' ,floatAge  )
print(' Sex    :',charSex + '\n','Child  : ',intChild  )
print('Married :',boolMarried)

# BIG INPUT STRING
bigString = "Ramakrishna Paramahansa;18 February 1836 – 16 August 1886, born Gadadhar Chattopadhyay, was an Indian mystic and yogi during the 19th century."
#PRINT THE ALL ELEMENTS 
print('\n')
print(bigString[0:143])
print('\n')
#COPY STRING TO A LIST
listStr = list(bigString)
print(listStr)
#JOIN LIST 
print('\n')
print("".join(listStr))

#FIND () AND COUNT()
print('\n')
print("FIND  'ram':",bigString.find("ram"))
print('\n')
print("COUNT 'a' :",bigString.count("a"))
print('\n')
print('TOTAL COUNT :',bigString.count(""))


#LENGTH OF THE STRING
print('\n')
print(len(bigString))
#LOWECASE 
print('\n')
print(bigString.lower())
#UPPERCASE 
print('\n')
print(bigString.upper())
print('\n')

#REPLACE 
print(bigString.replace("Chattopadhyay","Chatterjee"))

#SPLIT
print(bigString.split())


