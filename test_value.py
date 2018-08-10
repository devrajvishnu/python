# Function definition is here
def changeme( mylist ):
   "This changes a passed list into this function"
   mylist.append([1,2,3,4]);
   #print "Values inside the function: ", mylist
   return

# Now you can call changeme function
mynewlist = [10,20,30]
print "Values before calling the function: ", mynewlist
changeme( mynewlist );
print "Values outside the function: ", mynewlist
