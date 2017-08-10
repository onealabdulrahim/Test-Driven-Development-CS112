from project3 import *

def draw(width, height, letter, number):
	tiles = create(width, height, number)
	result = ""
	row = 0
	while (row < height):
		col = 0
		while (col < width):
			tile = row*width + col + 1
			if (tile in tiles):
				result = result + letter
			else:
				result = result + ' '
			col = col + 1
		result = result + '\n'
		row = row + 1			
	return result
	
def soften(grid):
	row = 0
	count = 0
	while(row < 3):
		col = 0
		while(col < 3):
			if (grid[row][col] != '_' and not(row == 1 and col == 1)):
				count = count + 1
			col = col + 1
		row = row + 1
	return count