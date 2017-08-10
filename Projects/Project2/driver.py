from project2 import *
import sys
import ast

result = ""
args = sys.argv			

cases = open("tests.txt")
testCases = cases.readlines()
failed = False

temp = []
for line in testCases:
	if len(line) > 3:
		if line[:-1] == "\n":
			temp.append(line[:-1])
		else:
			temp.append(line)
			
testCases = temp
	
ctr = 0
while ctr < len(testCases):
	args = ['null','null']
	test = testCases[ctr]
	pieces = testCases[ctr].split()
	
	if pieces[0] == "stop":
		break

	if pieces[0] == "isEmptyOnThree":						
		result = isEmptyOnThree(int(pieces[1]), int(pieces[2]))
	elif pieces[0] == "checkTile":						
		result = checkTile(int(pieces[1]), pieces[2])		
	else:
		print "Error: could not find the function " + str(pieces[0])
	ctr += 1
	expected = testCases[ctr][:-1]
	
	print "For (" + str(test[:-1]) + "):"
	print "\tExpected: \n'"+str(expected)+"' and got \n'"+str(result)+"'"

	if str(expected) == str(result):
		print "\t...passed..."
	else:
		print "\t...FAILED!!......................................."
		failed = True
	ctr += 1

if failed:
	print "XXXXXXX AT LEAST ONE TEST CASE FAILED XXXXXXX"
else:
	print " :-) :-) :-) ALL TESTS PASSED :-) :-) :-)"

#print result