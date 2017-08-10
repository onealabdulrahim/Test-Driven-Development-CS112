from project3 import *

def draw (width, height, letter, number):
	result = ""
	#utilizes the list result of create() depending on "number"
	if (number == "one"):
		listOf = create(width, height, "one")
	if (number == "two"):
		listOf = create(width, height, "two")
	if (number == "three"):
		listOf = create(width, height, "three")
	if (number == "four"):
		listOf = create(width, height, "four")
	if (number == "five"):
		listOf = create(width, height, "five")
		
	tile = 1
	#loop walks through all numbers of the result of create()
	while (tile <= width*height):
		#if tile is included within listOf (meaning it is a filled tile), 
		#we add the letter to our running String
		if (tile in listOf):
			result = result + str(letter)
		#otherwise, if tile is NOT within listOf (meaning it is a blank tile),
		#we add a space to our running String
		else:
			result = result + " "
		#we also check to see if we're at the edge, and add a line break if true
		if (tile % width == 0):
			#NOTE: line break will be appended to result every time
			result = result + "\n"
		tile = tile + 1
	return result
	
def soften(grid):
	count = 0
	walk = 0
	#the outerMiddle is the middle element in the larger list
	outerMiddle = (len(grid)) / 2
	#while loop to walk through the outer loop
	while (walk < len(grid)):
		innerWalk = 0
		#the innerMiddle is the middle element in the smaller lists within grid
		innerMiddle = len(grid[walk]) / 2
		#while loop to walk through inner loops
		while (innerWalk < len(grid[walk])):
			#if there is anything but an underscore...
			if (grid[walk][innerWalk] != "_"):
				#check to make sure we're not in the middle of middles
				#aka the most middle "tile", which is the fifth one in our case
				#if we are found to be in the middle, we decrement our counter...
				if (walk == outerMiddle and innerWalk == innerMiddle):
					count = count - 1
				#then we increment our counter
				#even if we visited the middle tile, the decrement would negate the increment,
				#effectively not counting the middle. (there must be a more elegant solution...)
				count = count + 1
			innerWalk = innerWalk + 1
		walk = walk + 1
	return count
