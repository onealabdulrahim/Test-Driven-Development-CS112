class Banner:
	def __init__(self, string):
		self.message = string
		self.dict = {}
		self.numbers = {}
	def addNumber(self, number, color):
		self.dict[number.getType()] = color
		self.numbers[str(number)] = number
	def __str__(self):
		string = ""
		string = string + self.message + " "
		i = 0
		keys = self.numbers.keys()
		while(i < len(keys)):
			string = string + (self.numbers[keys[i]]).draw() + " "
		return string