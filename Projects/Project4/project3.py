def create (width, height, number):
	result = []
	
	#ripped code from Dr. Dobolyi for "one" and "two" because
	#I don't trust my own algorithms :)
	
	#many of these involved copy+pasting the loops
	
	#half is the middle row number
	half = (height + 1) / 2
	
	#one condition
	if (number == "one"):
		ctr = 1
		#the final column is always filled
		while (ctr <= height):
			result.append(width*ctr)
			ctr = ctr + 1
	#two condition
	if (number == "two"):
		ctr = 1
		#creates top row
		while (ctr <= width):
			result.append(ctr)
			ctr = ctr + 1
		ctr = width - 1
		rowEnd = width * height
		#creates bottom row
		while (ctr >= 0):
			 result.append(rowEnd - ctr)
			 ctr = ctr - 1		 
	
	#still on two condition
	if (number == "two"):
		ctr = 1
		start = (half - 1) * width + 1
		#creates middle
		while (ctr < (width-1)):
			if (ctr+start) not in result:
				result.append(ctr+start)
			ctr = ctr + 1
		ctr = 0
		#creates edges
		while (ctr < height):
			new = ctr*width + 1
			if (ctr + 1 > half):
				if new not in result: 
					result.append(new)
			if (ctr < half):
				if (new-1) not in result and (new-1) > 0: 
					result.append(new-1)	
			ctr = ctr + 1
	
	#three condition
	if (number == "three"):
		ctr = 1
		#creates top row
		while (ctr <= width):
			result.append(ctr)
			ctr = ctr + 1
		ctr = width - 1
		rowEnd = width * height
		#creates bottom row
		while (ctr >= 0):
			 result.append(rowEnd - ctr)
			 ctr = ctr - 1
		ctr = (half - 1) * width + (width / 2) + 1
		#creates middle
		while (ctr <= half * width):
			result.append(ctr)
			ctr = ctr + 1
		ctr = width
		#creates edges
		while (ctr <= height * width):
			if ctr not in result:
				result.append(ctr)
			ctr = ctr + width
	
	#four condition
	if (number == "four"):
		ctr = 1
		#creates top row
		while (ctr <= width):
			result.append(ctr)
			ctr = ctr + (width - 1)
		ctr = (half - 1) * width + 1
		#creates middle row
		while (ctr <= half * width):
			result.append(ctr)
			ctr = ctr + 1
		ctr = width
		#creates right edge
		while (ctr <= width*height):
			if (ctr not in result):
				result.append(ctr)
			ctr = ctr + width
		ctr = width + 1
		#creates left edges
		while (ctr <= (half-1)*width):
			if (ctr not in result):
				result.append(ctr)
			ctr = ctr + (width-1)
	
	#five condition
	if (number == "five"):
		ctr = 1
		#creates top row
		while (ctr <= width):
			result.append(ctr)
			ctr = ctr + 1
		ctr = (half - 1) * width + 1
		#creates middle row
		while (ctr <= half * width):
			result.append(ctr)
			ctr = ctr + 1
		ctr = width + 1
		#creates left edges
		while (ctr <= (half-1)*width):
			if (ctr not in result):
				result.append(ctr)
			ctr = ctr + width
		ctr = width - 1
		rowEnd = width * height
		#creates bottom row
		while (ctr >= 0):
			result.append(rowEnd - ctr)
			ctr = ctr - 1
		ctr = (half+1)*width
		#creates right edge
		while (ctr <= width*height):
			if (ctr not in result):
				result.append(ctr)
			ctr = ctr + width
	return sorted(result)