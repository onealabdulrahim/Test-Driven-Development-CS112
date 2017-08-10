def main():
	try:
		file = open('file.txt') 
		lines = file.readlines()
	except:
		print "Couldn't find file.txt in this directory. Please try again."
		lines = []

	ctr = 0
	while (ctr < len(lines)):
		print "I read in : " + str(lines[ctr][:-1])
		ctr = ctr + 1

main()
 