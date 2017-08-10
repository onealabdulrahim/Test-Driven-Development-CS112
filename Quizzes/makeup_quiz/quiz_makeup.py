'''
Write code that walks over a two dimensional list of integers, and checks to see if a
neighbor of an element (so to its right or left) is negative; if so, it prints out the
current element and the negative neighbor.

For example:
checkNeighbors([[1,-1]]) --> '1 has -1, '
checkNeighbors([[-1,1,-2],[-1,-1]]) --> '1 has -1, 1 has -2, -1 has -1, -1 has -1, '
'''

# this function prints out all the negative neighbors of each element of a 2D list
# passed in as an argument

def checkNeighbors(list):
	result = ""	
	x = 0
	while (x < len(list)):
		y = 0
		while (y < len(list[x])):
			if (y != 0 and list[x][y-1] < 0):
				result = result + str(list[x][y]) + " has " + str(list[x][y-1]) + ", "
			if (y != (len(list[x]) - 1) and list[x][y+1] < 0):
				result = result + str(list[x][y]) + " has " + str(list[x][y+1]) + ", "
			y += 1
		x += 1			
	return result










		

