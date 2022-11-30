import random

def generateRandomPuzzle():
	# Setup.
	cars = ["B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T"]
	matrix = [
				[".", ".", ".", ".", ".", "."],
				[".", ".", ".", ".", ".", "."],
				[".", ".", ".", ".", ".", "."],
				[".", ".", ".", ".", ".", "."],
				[".", ".", ".", ".", ".", "."],
				[".", ".", ".", ".", ".", "."]
			]
	carsAdded = list()

	# Adding A.
	addCarToVector(matrix[2], "A", 2, True)

	# Randomly adding other cars.
	numOfCars = random.randint(8,15)
	for i in range(numOfCars):
		isVertical = random.randint(1,2) == 1 # Coin flip.

		if isVertical:

			# Creating column.
			columnIndex = random.randint(0,5)
			column = [0,0,0,0,0,0]
			for j in range(6):
				column[j] = matrix[j][columnIndex]

			vec = addCarToVector(column, cars[i], random.randint(2,3))

			# Mapping values back to original.
			if vec is not None:
				for j in range(6):
					matrix[j][columnIndex] = vec[j]
		else:
			rowIndex = random.randint(0,5)
			vec = addCarToVector(matrix[rowIndex], cars[i], random.randint(2,3), rowIndex == 2)

		if vec is not None:
			carsAdded.append(cars[i])
	
	# Joining matrix.
	stringifiedMatrix = ""
	for row in matrix:
		stringifiedMatrix += "".join(row)
	
	stringifiedFuel = ""
	for car in carsAdded:
		stringifiedFuel += f" {car}{random.randint(0,100)}"

	return stringifiedMatrix + stringifiedFuel


def findAllInstances(stringToSearch:str, substr:str):
	indices = list()
	start = 0

	while True:
		start = stringToSearch.find(substr, start)

		if start == -1:
			return indices

		indices.append(start)
		start += 1
	
	return indices


def addCarToVector(vector:list, car:str, carLength:int, shouldIgnoreEnd=False):
	stringifiedVector = "".join(vector)[:5] if shouldIgnoreEnd else "".join(vector)
	index = stringifiedVector.find("." * carLength)

	if index == -1:
		return None
	
	indices = findAllInstances(stringifiedVector, "." * carLength)

	indexToPlace = random.randint(0, len(indices) - 1)
	for i in range(carLength):
		vector[indices[indexToPlace] + i] = car

	return vector
	
	
	



	