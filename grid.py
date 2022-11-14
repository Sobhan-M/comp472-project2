from car import *

class Grid:
	def __init__(self, string:str):
		self.grid = stringToGrid(string)

	def __str__(self):
		message = ""
		for row in self.grid:
			message += "  ".join(row) + "\n"
		return message

	def __eq__(self, other):
		if not isinstance(other, Grid):
			return False

		if len(self.grid) != len(other.grid):
			return False

		for i in range(len(self.grid)):
			if len(self.grid[i]) != len(other.grid[i]):
				return False
			for j in len(self.grid[i]):
				if self.grid[i][j] != other.grid[i][j]:
					return False
		
		return True

	def updateGrid(self, car:Car):
		for i in self.grid:
			for j in self.grid:
				if self.grid[i][j] == car.symbol:
					self.grid[i][j] = "."

		if car.isAtExit():
			return

		for position in car.positions:
			self.grid[position[0]][position[1]] = car.symbol
	
def stringToGrid(string:str):
	grid = []
	for i in range(0,6):
		grid.append([])
		for j in range(0,6):
			grid[i].append(string[i*6+j])
	return grid