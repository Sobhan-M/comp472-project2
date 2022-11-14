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
	
	def __eq__(self, other):
		if not isinstance(other, Node):
			return False

		if self.grid != other.grid:
			return False

		if len(self.cars) != len(other.cars):
			return False

		for i in range(len(self.cars)):
			if self.cars[i] != other.cars[i]:
				return False

		return True
	
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

