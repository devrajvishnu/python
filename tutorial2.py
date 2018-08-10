###########################################################################################################################
#                                                                                                                         #  
#                                                                                                                         #
#                                                   TUTORIAL - 2                                                          #
#                                                                                                                         #
#                                                                                                                         # 
###########################################################################################################################
#CREATE A TUPLE
tuple = ('Devraj',27,'Kolkata','WB')
print(type(tuple))
print(tuple)
#SEARCHING ELEMENTS 
print (tuple[0:4])
print (tuple[0])
print (tuple[1])
print (tuple[2])
print (tuple[3])

tupleEx = tuple[1]
print(tupleEx)

#CREATE A LIST
listEx = ['Devraj',27,'Kolkata','WB']
print(type(listEx))
#print(listEx)
#SEARCHING ELEMENTS 
print(listEx[-1])
print(listEx[3])
print(listEx[-2])
print(listEx[2])
print(listEx[-3])
print(listEx[1])
print(listEx[-4])
print(listEx[0])

#STRING

listEx = ['Devraj',27,'Kolkata','WB']

#STRING CONVERSION

listName = list(listEx[0])
print(listName)

#JOIN A STRING

listName[6:] ="Vishnu"
print(listName)
print(" ".join(listName))

#LIST 
octList = ["Durgapur",713204,"Asansol",713304]
print(octList)
print(type(octList))

print(octList[0])

numStr1 = list(octList[0])
numStr2 = int(octList[1])
numStr3 = list(octList[2])
numStr4 = int(octList[3])
print(numStr1)
print(numStr2)
print(numStr3)
print(numStr4)


#INSERT ,APPEND ,SORT ,REMOPVE FROM A LIST 
octList = ['d','u', 'r', 'g', 'a', 'p', 'u', 'r']
octList.sort()
print(octList)

octList.append("k")
octList.append("m")

print(octList)
octList.remove(octList[8])
octList.remove("m")
octList.insert(2,'z')
octList.remove("z")

print(octList)

#INDEX LIST 
IndexList = [['1','2','3'],
             ['4','5','6'],
             ['a','b','c'],
             ['f','g','t']]

print(IndexList[2][1],IndexList[2][0],IndexList[3][2])
print(IndexList[2][1])
print(IndexList[2][0])
print(IndexList[3][2])





