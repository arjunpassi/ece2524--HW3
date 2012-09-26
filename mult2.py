# ECE 2524 Homework 3 Problem 2 Arjun Passi

import fileinput
import sys
import argparse


ans=1
inputFlag = 1
inputNum = 0

blankFlag = 0
nonNumericFlag = 0
count = 0
index = 0

parser = argparse.ArgumentParser(description='Process some numbers')

parser.add_argument('--ignore-non-numeric', action='store_const',const=1,default=0)

parser.add_argument('--ignore-blank', action='store_const',const=1,default=0)

parser.add_argument('input', nargs='*', type=str)

args = parser.parse_args()


if args.ignore_blank == 1 :
	blankFlag = 1

if args.ignore_non_numeric==1 :
	nonNumericFlag =1
if len(sys.argv) > 1:
   
   for line in fileinput.input(args.input):
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
	        number = float(inputNum)
	        ans = ans * number
	    

    except ValueError as e:
	
	    print e	
	    sys.exit(1)

    except EOFError:	    
	    print ans

