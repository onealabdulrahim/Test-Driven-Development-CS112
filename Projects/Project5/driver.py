from number import *
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

	if pieces[0] == "Number.__init__":	
		number = Number(pieces[1], pieces[2], int(pieces[3]), int(pieces[4]))
		if pieces[5] == "Number.__str__":				
			result = str(number)	
		if pieces[5] == "Number.draw()":				
			result = number.draw()			
		elif pieces[5] == "Number.getSoften()":
			result = number.getSoften()
		elif pieces[5] == "Number.getColor()":
			result = number.getColor()			
		else:
			result = "ERROR second function not recognized"
	elif pieces[0] == "Number.draw()":
		result = number.draw()				
	elif pieces[0] == "Number.match":		
		try:				
			number.match(eval(pieces[1]))
			if pieces[2] == "Number.getType()":
				result = number.getType()
			elif pieces[2] == "Number.getWidth()":
				result = number.getWidth()
			elif pieces[2] == "Number.getHeight()":
				result = number.getHeight()
			elif pieces[2] == "Number.getSoften()":
				result = number.getSoften()		
			elif pieces[2] == "Number.getColor()":
				result = number.getColor()	
			else:
				result = "ERROR second function not recognized"								
		except:
			result = "EXCEPTION"
	elif pieces[0] == "main":
		try:
			result = main(pieces[1])
		except IOError:
			result = "IOEXCEPTION"
		except ZeroDivisionError:
			result = "ZEROEXCEPTION"
		except Exception as e:
			result = "error " + str(e)
	else:
		print "Error: could not find the function " + str(pieces[0])
		
	
	ctr += 1

	if (len(pieces) > 5 and pieces[5] == "Number.draw()"):	
		expected = eval(testCases[ctr])
		print "here " + str(expected)
	elif ("Banner" in pieces[0] or pieces[0] == "Number.draw()"):
		expected = eval(testCases[ctr])
	elif (pieces[0] == "Number.match") and (pieces[2] == "Number.getType()" or pieces[2] == "Number.getColor()"):	
		expected = testCases[ctr][1:-2]
	elif pieces[0] == "Number.__init__" and pieces[5] == "Number.getColor()":
		expected = testCases[ctr][1:-2]
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