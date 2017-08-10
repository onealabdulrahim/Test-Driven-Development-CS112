def create (width, height, number):
	result = []
	half = (height + 1) / 2
	if (number == "one"):
		ctr = 1
		while (ctr <= height):
			result.append(width*ctr)
			ctr = ctr + 1
	elif (number == "two" or number == "three" or number == "five"):
		ctr = 1
		while (ctr <= width):
			result.append(ctr)
			ctr = ctr + 1
		ctr = width - 1
		rowEnd = width * height
		while (ctr >= 0):
			 result.append(rowEnd - ctr)
			 ctr = ctr - 1
			 
	if (number == "four" or number == "three" or number == "five"):
		ctr = 1
		while (ctr < height):
			new = ctr*width			
			if new not in result: 
				if (number != "five"):
					result.append(new)
				elif (new > half*width):
					result.append(new)
			ctr = ctr + 1			 
		
	if (number == "two"):
		ctr = 1
		start = (half - 1) * width + 1
		while (ctr < (width-1)):
			if (ctr+start) not in result:
				result.append(ctr+start)
			ctr = ctr + 1
		ctr = 0
		while (ctr < height):
			new = ctr*width + 1
			if (ctr + 1 > half):
				if new not in result: 
					result.append(new)
			if (ctr < half):
				if (new-1) not in result and (new-1) > 0: 
					result.append(new-1)	
			ctr = ctr + 1	
	elif (number == "three"):
		ctr = 1
		start = (half - 1) * width + width / 2
		while (ctr < (width+1)/2):
			if (ctr+start) not in result:
				result.append(ctr+start)
			ctr = ctr + 1
	elif (number == "four" or number == "five"):
		ctr = 0
		start = (half - 1) * width + 1
		while (ctr < (width)):
			if (ctr+start) not in result:
				result.append(ctr+start)
			ctr = ctr + 1		
		ctr = 0
		while (ctr < height):
			new = ctr*width + 1
			if (ctr < half):
				if (new) not in result and (new) > 0: 
					result.append(new)	
			ctr = ctr + 1	
		if (width*height) not in result:	
			result.append(width*height)
			
	return sorted(result)