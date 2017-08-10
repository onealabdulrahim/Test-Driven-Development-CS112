def create (width, height, number):
	result = []
	
	#filled tiles for when number is "one"
	if (number == "one"):
		ticker = width
		while ticker <= (width * height):
			result.append(ticker)
			ticker = ticker + width
	
	#filled tiles for when number is "two"
	if (number == "two"):
		ticker = 1
		#the first row for "two" is always filled
		while ticker < (width):
			result.append(ticker)
			ticker = ticker + 1
			
		#the last row for "two" is always filled
		ticker = ((width * (height - 1)) + 2)
		while ticker <= (width * height):
			result.append(ticker)
			ticker = ticker + 1
			
		#the middle row differs based on height
		if (height % 2 == 0):
			middleRow = (height / 2) - 1
		else:
			middleRow = (height / 2)
		ticker = middleRow * width + 2
		while (ticker <= (((middleRow + 1) * width) - 1)):
			result.append(ticker)
			ticker = ticker + 1
			
		#the sides differ based on middleRow and height
		ticker = width
		while (ticker <= (middleRow * width)):
			result.append(ticker)
			ticker = ticker + width
		ticker = (middleRow + 1) * width + 1
		while (ticker <= (width * height)):
			result.append(ticker)
			ticker = ticker + width
	return sorted(result)
	
