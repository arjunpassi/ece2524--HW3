# ECE 2524 Homework 3 Problem 1 Arjun Passi

import argparse
import sys

parser = argparse.ArgumentParser(description='Process some numbers')
args = parser.parse_args()

ans=1
inputFlag = 1
inputNum = 0

try:	
	while inputFlag == 1:
	    inputNum = raw_input()
	    str = inputNum
	    
	    if str.strip() == "":
	        print ans
	        ans = 1
	        continue
	    
	    number = float(inputNum)
	    ans = ans * number
	    

except ValueError as e:	
	print e	
	sys.exit(1)

except EOFError:
	print ans



