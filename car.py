import numpy as np
from position import *
from iomanager import *

EXIT_POSITION = np.array([2,5])

class Car:
	def __init__(self, positions:Position, length:int, orientation:str, symbol:str, fuel=100):
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
		return f"{self.symbol}:{self.fuel}"

	def __eq__(self, other):
		if not isinstance(other, Car):
			return False
		
		if not self.positions == other.positions:
			return False

		if self.length != other.length:
			return False

		if self.orientation != other.orientation:
			return False

		if self.symbol != other.symbol:
			return False

		# if self.fuel != other.fuel:
		# 	return False

		return True

	
	def move(self, moveDistance:int):
		"""
		Moves the car moveDistance blocks based on orientation.
		If oriented horizontally, then positive is to the right.
		If oriented vertically, then positive is downward.
		"""
		if self.orientation == "x":
			self.positions.translate((0, moveDistance))
		else:
			self.positions.translate((moveDistance, 0))
		
		self.fuel -= abs(moveDistance)

	def copy(self):
		return Car(self.positions.copy(), self.length, self.orientation, self.symbol, self.fuel)

	def nextPosition(self, moveDistance:int):
		"""
		Returns the change in position, without actually applying it or adjusting fuel.
		"""
		newPositions = self.positions.copy()

		if self.orientation == "x":
			newPositions.translate((0, moveDistance))
		else:
			newPositions.translate((moveDistance, 0))

		return newPositions

	def canUseFuel(self, fuelToUse:int):
		return self.fuel - abs(fuelToUse) >= 0

	def isAtExit(self):
		for coord in self.positions.position:
			if len(coord) != 2:
				return False		
			if EXIT_POSITION[0] == coord[0] and EXIT_POSITION[1] == coord[1]:
				return True
		return False

def findCarSymbols(string:str):
	symbols = []
	characters = set(string)
	
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

def generateCarList(puzzleLine:str):
	grid = getGrid(puzzleLine)
	carFuel = getFuel(puzzleLine)

	carSymbols = findCarSymbols(grid)
	carPositions = findCarPositions(grid, carSymbols)
	carOrientations = findCarOrientations(carPositions)
	carLengths = findCarLengths2(carPositions)

	cars = list()
	for i in range(len(carSymbols)):
		fuel = 100 if carFuel.get(carSymbols[i]) is None else carFuel.get(carSymbols[i])
		cars.append(Car(Position(carPositions[i]), carLengths[i], carOrientations[i], carSymbols[i], fuel))

	return cars

def getCarFromList(carSymbol:str, cars:list):
	for car in cars:
		if car.symbol == carSymbol:
			return car
	return None