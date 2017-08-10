import sys
import ast

from quiz1 import *

# Prepare to process the input file
cases = open("tests.txt")
testCases = cases.readlines()
cases.close()
failed = False
ctr = 0
ctrfail = 0

while ctr < len(testCases):
	# Get current test case: "output = func_name(input)"
	test = testCases[ctr]
	func_name = test.split()[0]
	# input = test[len(func_name):-1]
	input = test.split()[1]
	output = testCases[ctr+1][:-1]
	ctr += 2
	
	# Test the student's code
	if func_name == "sum_three_digit":
		input = ast.literal_eval(input)
		result = sum_three_digit(input)		
		expected = ast.literal_eval(output)
		
		print "For the input:\t", input
		print "---We expected:\t", expected
		print "---Your result:\t", result
		if result != expected:
			failed = True
			ctrfail += 1
	# Extend if there are more than one functions to test
	else:
		print "Error: could not find the required function"
		
	# Error information for current test case
	if failed == True:
		print "\t...FAILED!!..."
	else:
		print "\t...pass..."
	failed = False

# Error information in general
if ctrfail > 0:
	print "XXXXXXX ", str(ctrfail), " TEST CASE FAILED XXXXXXX"
	print "Please correct your bug, or you will get 0/5 for this assignment"
else:
	print " :-) :-) :-) ALL ", str(int(ctr/2)), " TESTS PASSED :-) :-) :-)"
	print "You will get 5/5 for this coding assignment"