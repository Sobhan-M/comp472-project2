class Position:
	def __init__(self, input):
		self.position = input

	def __eq__(self, other):
		if not isinstance(other,Position):
			return False
		if len(self.position) != len(other.position):
			return False
		for i in range(len(self.position)):
			if len(self.position[i]) != len(other.position[i]):
				return False
			for j in range(len(self.position[i])):
				if self.position[i][j] != other.position[i][j]:
					return False
		return True

	def copy(self):
		positionCopy = []
		for coord in self.position:
			positionCopy.append([coord[0],coord[1]])
		return Position(positionCopy)
	
	def __str__(self):
		return str(self.position)

	def translate(self, vector:tuple):
		for i in range(len(self.position)):
			for j in range(len(self.position[i])):
				self.position[i][j] = self.position[i][j] + vector[j]

