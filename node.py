from car import *
import numpy as np

GRID_MIN = 0
GRID_MAX = 5

class Node:
	def __init__(self, parent, children, grid, cars):
		self.parent = parent
		self.children = children
		self.grid = grid
		self.cars = cars
	
	def canMove(self, car:Car, numOfMoves):

		newPosition = car.nextPosition(numOfMoves)

		canUseFuel = car.canUseFuel(numOfMoves)
		hasNoConflict = not hasPositionConflict(self.cars, car.symbol, newPosition)
		isWithinBounds = isInBorder(newPosition)		

		return canUseFuel and isWithinBounds and hasNoConflict
	
	def isGoal(self):
		for car in self.cars:
			if car.symbol == "A":
				return False
		return True
	
	def getHeuristic():
		# Will depend on the heuristic.
		return

	def generateChild():
		# Create a new node after the car moves.
		return

	def isRoot(self):
		return self.parent is None

def isInBorder(positions):
	for pos in positions:
		# Checking if position is within borders.
		if GRID_MIN <= pos[0] and pos[0] <= GRID_MAX:
			if GRID_MIN <= pos[1] and pos[1] <= GRID_MAX:
				continue
		return False
	return True

def hasPositionConflict(cars, carSymbol, newPosition):
	for pos in newPosition:
		for car in cars:
			if car.symbol != carSymbol: # Do not compare position with self.
				if pos in car.positions:
					return False
	return True

