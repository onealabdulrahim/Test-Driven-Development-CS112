from project4 import *
import sys
import ast

result = ""
args = sys.argv			

cases = open("tests.txt")
testCases = cases.readlines()
failed = False

temp = []
for line in testCases:
	if len(line) >= 1:
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

	if pieces[0] == "draw":						
		result = draw(int(pieces[1]), int(pieces[2]), pieces[3], pieces[4])	
	elif pieces[0] == "soften":						
		result = soften(ast.literal_eval(testCases[ctr][7:]))	
	elif pieces[0] == "create":						
		result = create(int(pieces[1]), int(pieces[2]), pieces[3])					
	else:
		print "Error: could not find the function " + str(pieces[0])
		
	
	ctr += 1

	if pieces[0] == "draw":
		expected = eval(testCases[ctr])
	else:
		expected = testCases[ctr][:-1]
	
	print "For (" + str(test[:-1]) + "):"
	if pieces[0] == "draw":
		print "\tExpected: \n'"+str(expected)+"' and got \n'"+str(result)+"'"
	else:
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