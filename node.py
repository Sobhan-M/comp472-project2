from car import *
from grid import *
from iomanager import *
import numpy as np

GRID_MIN = 0
GRID_MAX = 5

class Node:
	def __init__(self, grid:Grid, cars:list, parent=None, children=[], move=""):
		self.parent = parent
		self.children = children
		self.grid = grid
		self.cars = cars
		self.move = move
		self.exitedCars = list()

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

	def __str__(self):
		return self.grid.lineString()

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

	def generateChild(self, car:Car, move:int):
		if move == 0:
			raise Exception("Cannot Generate A Child Without A Move")

		if not canMove(car, move, self.cars):
			return None
		
		newCar = car.copy()
		newCar.move(move)
		newGrid = self.grid.copy()
		newGrid.updateGrid(newCar)
		newCars = copyCarsList(self.cars)

		exitingCar = None
		
		# Updating cars list.
		for i in range(len(newCars)):
			if newCars[i].symbol == car.symbol:
				if newCar.isAtExit() and newCar.orientation == "x" and newCar.symbol != "A":
					exitingCar = newCars.pop(i)
					break
				else:
					newCars[i] = newCar

		newNode = Node(newGrid, newCars, self)
		newNode.move = moveFromParent(car, move)

		if exitingCar is not None:
			newNode.exitedCars.append(exitingCar)

		self.children.append(newNode)
		return newNode

	def expandChildren(self):
		children = []

		for car in self.cars:
			for move in [4,3,2,1,-1,-2,-3,-4]:
				child = self.generateChild(car, move)
				if child is not None:
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
	for pos in positions.position:
		# Checking if position is within borders.
		if GRID_MIN <= pos[0] and pos[0] <= GRID_MAX:
			if GRID_MIN <= pos[1] and pos[1] <= GRID_MAX:
				continue
		return False
	return True

def hasPositionConflict(cars, carSymbol, newPosition):
	for pos in newPosition.position:
		for car in cars:
			if car.symbol != carSymbol: # Do not compare position with self.
				for coord in car.positions.position:
					if pos[0] == coord[0] and pos[1] == coord[1]:
						return True
	return False

def canMove(car:Car, numOfMoves:int, cars:list):
		# Checking each position along the way.
		if numOfMoves < 0:
			start = numOfMoves
			end = 0
		else:
			start = 0
			end = numOfMoves
		
		for intermediateMove in range(start, end):
			intermediatePosition = car.nextPosition(intermediateMove)
			if hasPositionConflict(cars, car.symbol, intermediatePosition):
				return False

		newPosition = car.nextPosition(numOfMoves)
		return car.canUseFuel(numOfMoves) and isInBorder(newPosition) and not hasPositionConflict(cars, car.symbol, newPosition)

def copyCarsList(cars):
	newCars = []
	for car in cars:
		newCars.append(car.copy())
	return newCars

def moveFromParent(car:Car, move:int):
		output = ""
		if car.orientation == "x" and move > 0:
			output = "{} {:>5} {}".format(car.symbol, "right", abs(move))
		elif car.orientation == "x" and move < 0:
			output = "{} {:>5} {}".format(car.symbol, "left", abs(move))
		elif car.orientation == "y" and move > 0:
			output = "{} {:>5} {}".format(car.symbol, "down", abs(move))
		elif car.orientation == "y" and move < 0:
			output = "{} {:>5} {}".format(car.symbol, "up", abs(move))

		return output

def generateStartNode(puzzleLine:str):
	return Node(Grid(getGrid(puzzleLine)), generateCarList(puzzleLine))





