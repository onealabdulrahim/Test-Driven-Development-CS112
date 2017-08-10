from project4 import *

class Number:
	def __init__(self,color,type,width,height):
		self.color = color
		self.type = type
		self.width = width
		self.height = height
		self.soften = False
		
	def match(self,list):
		tilesIn = []
		row = 0
		while (row < len(list)):
			col = 0
			width = len(list[row])
			while (col < width):
				if list[row][col] != '_':
					tilesIn.append(row*width + col + 1)
				col = col + 1
			row = row + 1
		tilesIn = sorted(tilesIn)
	
		shapes = ["one", "two", "three", "four", "five"]
		while width < 10:
			height = 3
			while height < 10:
				ctr = 0
				while ctr < len(shapes):
					tiles = create(width,height,shapes[ctr])
					if tiles == tilesIn:
						self.type = shapes[ctr]
						self.width = width
						self.height = height						
						return
					ctr = ctr + 1
				height = height + 1
			width = width + 1

		raise Exception()
		
	def draw(self):
		result = draw(self.width,self.height,self.color,self.type)
		return result
	
	def getType(self):
		return self.type
		
	def getWidth(self):
		return self.width
		
	def getHeight(self):
		return self.height
		
	def getColor(self):
		return self.color
		
	def getSoften(self):
		return self.soften				
	
	def __str__(self):
		return self.color + " " + self.type