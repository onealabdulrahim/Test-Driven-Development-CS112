'''--Instruction
You are required to write Python code to complete Exercise 6 in introduction
Chapter in the textbook
"6. Gets an three-digit integer from the user, and adds together all of its digits. 
For example, 123 would return 6. Hint: remember you can use division!"

--Details 
'num' below will store some integer that 0 <= num < 1000 at the beginning
After the calculation of your code, 'sum' should store an integer that 
is the sum of all num's three digits
For example, if num = 123, then sum = 1+2+3 = 6; if num = 6, then sum = 0+0+6 = 6

--Hint
Operators such as '//', '%' will be useful. 
Simple example: since 16 = 5*3 + 1, we have 16 % 5 = 1, 16 // 5 = 3
'''

def sum_three_digit(num):	
	
	# YOUR CODE GOES BELOW HERE
	
	# You only need to complete lines 25 and 29 to do the required tasks
	
	# Get the digit in hundreds position, 1 if num = 123
	hundreds = num // 100
	# Get the digit in tens position, 2 if num = 123
	tens = (num // 10) % 10
	# Get the digit in units position, 3 if num = 123
	units = num - (hundreds * 100) - (tens * 10)
	# Add them together, and evaluate it to 'sum', 6 if num = 123
	sum = hundreds + tens + units
	
	# DO NOT WRITE CODE BELOW THIS LINE	
	
	return sum