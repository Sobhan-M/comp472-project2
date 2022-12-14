from position import *
from grid import *
from node import *
from car import *
import time

class Reporter:
	"""
	A method that records information about the solving of an algorithm and helps write the associated report.
	Essentially an observer.
	"""
	def __init__(self, puzzleLine:str):
		self.puzzleLine = puzzleLine
		self.startNode = generateStartNode(puzzleLine)
		self.startTime = 0
		self.endTime = 0
		self.nodesVisited = 0
		self.solutionPath = list()
		self.searchPath = list()
	
	def startTimer(self):
		self.startTime = time.time()
	
	def endTimer(self):
		self.endTime = time.time()

	def timeElapsed(self):
		return self.endTime - self.startTime

	def countVisit(self):
		self.nodesVisited += 1

	def setGoalNode(self, goal:Node):
		self.goalNode = goal

		if goal is not None:
			self.solutionPath = generatePathFromRoot(goal)

	def countTotalMoves(self):
		return len(self.solutionPath) - 1
	
	def getMovesInPath(self):
		moves = list()
		for node in self.solutionPath[1:]:
			moves.append(node.move)
		return moves

	def initialConfigurationMessage(self):
		output = f"Initial board configuration: {self.puzzleLine}\n"
		output += f"\n{str(self.startNode.grid)}\n"
		output += f"Car fuel available: "
		cars = self.startNode.cars
		for i in range(len(cars)):
			output += str(cars[i])
			if i != len(cars)-1:
				output += ", "
		output += "\n\n"
		return output

	def runtimeMessage(self):
		return f"Runtime: {self.timeElapsed()} seconds\n"

	def searchPathMessage(self):
		return f"Search path length: {self.nodesVisited} states\n"
	
	def solutionLengthMessage(self):
		return f"Solution path length: {self.countTotalMoves()} moves\n"

	def solutionPathMessage(self):
		return "Solution path: " + "; ".join(self.getMovesInPath()) + "\n"

	def solutionPathStatesMessage(self):
		output = "\n"

		for state in self.solutionPath[1:]:
			car = getCarFromList(state.move[0], state.cars)
			if car is None:
				car = getCarFromList(state.move[0], state.exitedCars)

			output += "{} {:>4} {}\n".format(state.move, car.fuel, str(state)) 
		
		output += "\n"

		return output

	def finalConfigurationMessage(self):
		return str(self.solutionPath[-1].grid) + "\n"

	def generateSolutionReport(self):
		report = self.initialConfigurationMessage()
		report += self.runtimeMessage()
		report += self.searchPathMessage()

		if self.goalNode is None:
			report += "\nNo solution was found for this puzzle.\n"
		else:
			report += self.solutionLengthMessage()
			report += self.solutionPathMessage()
			report += self.solutionPathStatesMessage()
			report += self.finalConfigurationMessage()

		return report

	def addToSearchPath(self, node:Node, f, g, h):
		fn = f(node)
		gn = g(node)
		hn = h(node)
		msg = "f: {:<4} g: {:<4} h: {:<4} {}".format(fn, gn, hn, str(node))
		self.searchPath.append(msg)

def generatePathFromRoot(goalNode: Node):
	node = goalNode
	path = []
	while not node.isRoot():
		path.insert(0, node)
		node = node.parent
	path.insert(0, node) # Including Root
	return path

	