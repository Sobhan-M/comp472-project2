from car import *
from grid import *
import numpy as np

GRID_MIN = 0
GRID_MAX = 5

class Node:
	def __init__(self, grid:Grid, cars:list, parent=None, children=[]):
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

	def copy(self):
		return Node(self.grid.copy(), copyCarsList(self.cars), self.parent, self.children)
	
	def isGoal(self):
		for car in self.cars:
			if car.symbol == "A":
				if car.isAtExit():
					return True
				else:
					return False

		# If A is not there, then automatically becomes the goal state.
		return True

	def generateChild(self, grid:Grid, car:Car, move:int, cars:list):
		if not canMove(car, move, cars):
			return None
		
		newCar = car.copy()
		newCar.move(move)
		newGrid = grid.copy()
		newGrid.updateGrid(newCar)
		newCars = copyCarsList(cars)
		
		# Updating cars list.
		for i in range(len(newCars)):
			if newCars[i].symbol == car.symbol:
				if newCar.isAtExit():
					newCars.pop(i)
				else:
					newCars[i] = newCar

		newNode = Node(newGrid, newCars, self)
		self.children.append(newNode)
		return newNode

	def expandChildren(self):
		children = []

		for car in self.cars:
			for move in [-4,-3,-2,-1,1,2,3,4]:
				child = self.generateChild(self.grid, car, move, self.cars)
				if not child is None:
					children.append(child)
					
		return children

	def isRoot(self):
		return self.parent is None

	def cost(self):
		if self.isRoot():
			return 0

		cost = 1
		parent = self.parent

		while not parent.isRoot():
			cost += 1
			parent = parent.parent
		
		return cost

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

def canMove(car:Car, numOfMoves:int, cars:list):
		newPosition = car.nextPosition(numOfMoves)
		return car.canUseFuel(numOfMoves) and isInBorder(newPosition) and not hasPositionConflict(cars, car.symbol, newPosition)

def copyCarsList(cars):
	newCars = []
	for car in cars:
		newCars.append(car.copy())
	return newCars






