class Grid:
	def __init__(self, string:str):
		self.grid = stringToGrid(string)

	def __str__(self):
		message = ""
		for row in self.grid:
			message += "  ".join(row) + "\n"
		return message
	
def stringToGrid(string:str):
	grid = []
	for i in range(0,6):
		grid.append([])
		for j in range(0,6):
			grid[i].append(string[i*6+j])
	return grid