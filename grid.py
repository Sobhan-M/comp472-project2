from car import *

class Grid:
	def __init__(self, grid):
		if isinstance(grid, str):
			self.grid = stringToGrid(grid)
		else:
			self.grid = grid

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
			for j in range(len(self.grid[i])):
				if self.grid[i][j] != other.grid[i][j]:
					return False
		
		return True

	def updateGrid(self, car:Car):
		"""
		Updates the grid after the car has moved.
		Replaces all old positions with '.'.
		Places symbol on all new positions.
		Removes car completely if it is at the exit.
		"""
		for i in range(len(self.grid)):
			for j in range(len(self.grid[i])):
				if self.grid[i][j] == car.symbol:
					self.grid[i][j] = "."

		if car.isAtExit():
			return

		for coord in car.positions.position:
			self.grid[coord[0]][coord[1]] = car.symbol

	def copy(self):
		newGrid = copyMatrix(self.grid)
		return Grid(newGrid)

def copyMatrix(matrix):
	newMatrix = []
	for i in range(len(matrix)):
		newMatrix.append([])
		for j in range(len(matrix[i])):
			newMatrix[i].append(matrix[i][j])
	return newMatrix


def stringToGrid(string:str):
	grid = []
	for i in range(0,6):
		grid.append([])
		for j in range(0,6):
			grid[i].append(string[i*6+j])
	return grid