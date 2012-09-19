# ECE 2524 Homework 3 Problem 2 Arjun Passi

import argparse
import sys
import fileinput


#parser = argparse.ArgumentParser(description='Process some numbers')
#parser = argparse.ArgumentParser()

#parser.add_argument('input', nargs = '*', type=argparse.FileType('r'))
#parser.add_argument('--ignore-blank', type=str,default=0)

#args = parser.parse_args()

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
        print blankFlag
    
    elif sys.argv[count] == "--ignore-non-numeric":
        nonNumericFlag = 1
        print nonNumericFlag
    
    else:
        fileArray.append(sys.argv[count])
        index = index + 1
    
    count = count + 1

fileArray.pop(0)   

print fileArray

if len(sys.argv) > 1:
   
   for line in fileinput.input(fileArray):
       try:
          print line
          inputNum = float(line)       
          str = line
          
          if blankFlag == 1:
                if str.strip() == "":
                    print "h"    
                
          ans = ans * inputNum          

       except ValueError as e:
       
            
            
                
	        print e	
	        sys.exit(1)                                        
	    	    
   print "\nAnswer :", ans
	

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
	    print "\nEnd of the File: Pressed CtrlD"
	    print "\nThe answer is  :", ans


