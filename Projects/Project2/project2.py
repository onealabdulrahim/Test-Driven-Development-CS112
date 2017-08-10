def checkTile(tile, number):
	if (tile == 1 or tile == 5):
		if (number != "one"):
			return True	
	if (tile == 2 or tile == 10 or tile == 11):
		if (number != "one" and number != "four"):
			return True	
	if (tile == 3 or tile == 12):
			return True
	if (tile == 4):
		if (number == "four" or number == "five"):
			return True	
	if (tile == 6 or tile == 9):
		if (number != "two"):
			return True	
	if (tile == 7):
		if (number == "two"):
			return True		
	return False
def isEmptyOnThree(tile, width):
	#stupidity input check
	if (tile <= 0 or tile > (width * 4) or (width == 2)):
		return "invalid"
	#row 1
	if (tile <= width):
		return False
	#row 2
	if (tile > width and tile <= (2 * width)):
		if (width % 2 == 0):
			if (tile > ((width * 2) - (width / 2))):
				return False
		else:
			if (tile >= ((width * 2) - (width / 2))):
				return False
	#row 3
	if (tile == (width * 3)):
		return False
	#row 4
	if (tile > (3 * width) and tile <= (4 * width)):
		return False
	return True