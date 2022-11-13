import numpy as np

EXIT_POSITION = np.array([2,5])

class Car:
	# Constructor. Pos is an array of position vectors.
	def __init__(self, pos:list, length:int, orientation:str, symbol:str, fuel=100):
		self.positions = pos
		self.length = length
		self.orientation = orientation
		self.symbol = symbol
		self.fuel = fuel

	# Moves the car moveDistance blocks based on orientation.
	# If oriented horizontally, then positive is to the right.
	# If oriented vertically, then positive is to the left.
	def move(self, moveDistance:int):
		if self.orientation == "x":
			for pos in self.positions:
				pos += np.array([0,moveDistance])
		else:
			for pos in self.positions:
				pos += np.array([moveDistance,0])
		
		self.fuel -= moveDistance

	def nextPosition(self, moveDistance:int):
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
