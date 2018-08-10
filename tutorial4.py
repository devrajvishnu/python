###########################################################################################################################
#                                                                                                                         #  
#                                                                                                                         #
#                                                   TUTORIAL - 4                                                          #
#                                                                                                                         #
#                                                                                                                         # 
###########################################################################################################################
# COMPILE - " python3 filename .py "
#  RUN - " sudo chmod a+x ./filename.py "

#WRITE A AGE IDENTIFICATION OF A PROGRAM IN PYTHON USING IF-ELIF-ELSE STATEMENT 
#IF-ELIF-ELSE STATEMENT

your_Age =int(input("Your Age is :"))
if (your_Age > 0) and (your_Age <100):
    if (your_Age == 27):
        print("Your age same as Me")
    elif(your_Age < 27):
        print("You are younger than Me")
    else:
        print("You are older than Me")
else:
        print("Don't lie about your age")
        
#CONDITIONAL EXPRESSION
x,y = 0,1
a = 'y is less than x 'if ( y < x )else 'x is less than y'
print(a)

#if-else 
student_Marks = float(input())
   
if(student_Marks >= 50) and (student_Marks <= 60):
    print("2nd Class")
elif(student_Marks >= 60) and (student_Marks <= 70):
    print("1st Class")
else:
    print("fail")