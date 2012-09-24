# ECE 2524 Homework 3 Problem 2 Arjun Passi

import argparse
import sys
import fileinput


ans=1
inputFlag = 1
inputNum = 0

blankFlag = 0
nonNumericFlag = 0
count = 0
index = 0

fileArray = []

while count < len(sys.argv):
    if sys.argv[count] == "--ignore-blank":
        blankFlag = 1
    
    elif sys.argv[count] == "--ignore-non-numeric":
        nonNumericFlag = 1
    
    else:
        fileArray.append(sys.argv[count])
        index = index + 1
    
    count = count + 1

fileArray.pop(0)   

if len(sys.argv) > 1:
   
   for line in fileinput.input(fileArray):
       try:
          str = line
          inputNum = float(line)                     
          ans = ans * inputNum          

       except ValueError as e:
       
            if blankFlag == 1:
                if str.strip() == "":
                    continue
            
            else:
                if str.strip() == "":
                    print ans
                    ans = 1
                    continue
            
            if nonNumericFlag == 1:
                    continue
                 
            print e
            sys.exit(1)                                             
	    	    
   print ans
	

else:

    try:	
	    while inputFlag == 1:
	        inputNum = raw_input("Enter Number: ")
	        number = float(inputNum)
	        ans = ans * number
	    

    except ValueError as e:
	
	    print e	
	    sys.exit(1)

    except EOFError:	    
	    print ans

