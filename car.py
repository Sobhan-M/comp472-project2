import numpy as np

EXIT_POSITION = np.array([2,5])

class Car:
	def __init__(self, positions:list, length:int, orientation:str, symbol:str, fuel=100):
		"""
		Positions is a list of positions.
		i.e. (y,x)
		"""
		self.positions = positions
		self.length = length
		self.orientation = orientation
		self.symbol = symbol
		self.fuel = fuel

	def __str__(self):
		return f"{self.symbol} {self.fuel}"

	def __eq__(self, other):
		if not isinstance(other, Car):
			return False
		
		if not arePositionsEqual(self.positions, other.positions):
			return False

		if self.length != other.length:
			return False

		if self.orientation != other.orientation:
			return False

		if self.symbol != other.symbol:
			return False

		if self.fuel != other.fuel:
			return False

		return True

	
	def move(self, moveDistance:int):
		"""
		Moves the car moveDistance blocks based on orientation.
		If oriented horizontally, then positive is to the right.
		If oriented vertically, then positive is to the left.
		"""
		if self.orientation == "x":
			for pos in self.positions:
				pos += np.array([0,moveDistance])
		else:
			for pos in self.positions:
				pos += np.array([moveDistance,0])
		
		self.fuel -= moveDistance

	def copy(self):
		return Car(copyPositions(self.positions), self.length, self.orientation, self.symbol, self.fuel)

	def nextPosition(self, moveDistance:int):
		"""
		Returns the change in position, without actually applying it or adjusting fuel.
		"""
		newPositions = []
		if self.orientation == "x":
			for pos in self.positions:
				newPositions.append(pos + np.array([0,moveDistance]))
		else:
			for pos in self.positions:
				newPositions.append(pos + np.array([moveDistance,0]))
		return newPositions

	def canUseFuel(self, fuelToUse:int):
		return self.fuel - fuelToUse >= 0

	def isAtExit(self):
		return EXIT_POSITION in self.positions

def findCarSymbols(string:str):
	symbols = []
	characters = set(string)
	# Create a car for each symbol.
	for character in characters:
		if character == ".":
			continue
		symbols.append(character)
	return symbols

def findCarPositions(string:str, symbols:list):
	allPositions = []
	for symbol in symbols:
		symbolPositions = []
		startIndex = 0
		index = 0
		while index != -1:
			index = string.find(symbol, startIndex)
			if index != -1:
				symbolPositions.append((index // 6, index % 6))
			startIndex = index + 1
		allPositions.append(symbolPositions)
	return allPositions

def findCarLengths1(string:str, symbols:list):
	lengths = []
	for symbol in symbols:
		lengths.append(string.count(symbol))
	return lengths

def findCarLengths2(positions):
	lengths = []
	for position in positions:
		lengths.append(len(position))
	return lengths

def findCarOrientations(positions):
	orientations = []
	for position in positions:
		if position[0][0] == position[1][0]: # The Ys match.
			orientations.append("x")
		else:
			orientations.append("y")
	return orientations

def generateCarList(string:str):
	carSymbols = findCarSymbols(string)
	carPositions = findCarPositions(string, carSymbols)
	carOrientations = findCarOrientations(carPositions)
	carLengths = findCarLengths2(carPositions)

	cars = list()
	for i in range(len(carSymbols)):
		cars.append(Car(carPositions[i], carLengths[i], carOrientations[i], carSymbols[i]))

	return cars

def copyPositions(positions:list):
	newPositions = []
	for position in positions:
		newPositions.append((position[0], position[1]))
	return newPositions

def arePositionsEqual(position1, position2):
	if len(position1) != len(position2):
		return False
	
	for i in range(len(position1)):
		if len(position1[i]) != len(position2[i]):
			return False
		for j in range(len(position1[i])):
			if position1[i][j] != position2[i][j]:
				return False
	
	return True