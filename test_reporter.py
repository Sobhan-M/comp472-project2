import unittest

from reporter import *
from position import *
from grid import *
from node import *
from car import *
import time

example = "C.B...C.BHHHAADD........EEGGGF.....F"

class TestReporter(unittest.TestCase):

	def test_timeElapsed(self):
		reporter = Reporter(example)

		startTime = time.time()
		reporter.startTimer()
		time.sleep(0.25)
		endTime = time.time()
		reporter.endTimer()

		self.assertAlmostEqual(reporter.timeElapsed(), endTime - startTime)

	def test_setGoalNode(self):
		parent = generateStartNode("C.B...C.BHHHAADD........EEGGGF.....F")
		child = parent.generateChild(getCarFromList("D", parent.cars), 2)
		goal = child.generateChild(getCarFromList("A", child.cars), 4)

		reporter1 = Reporter(example)
		reporter1.setGoalNode(goal)
		self.assertIs(reporter1.goalNode, goal)
		self.assertIs(reporter1.solutionPath[2], goal)
		self.assertIs(reporter1.solutionPath[1], child)
		self.assertIs(reporter1.solutionPath[0], parent)

		reporter2 = Reporter(example)
		reporter2.setGoalNode(None)
		self.assertIsNone(reporter2.goalNode)
		self.assertEqual(reporter2.solutionPath, [])

	def test_countTotalMoves(self):
		parent = generateStartNode("C.B...C.BHHHAADD........EEGGGF.....F")
		child = parent.generateChild(getCarFromList("D", parent.cars), 2)
		goal = child.generateChild(getCarFromList("A", child.cars), 4)
		reporter = Reporter(example)
		reporter.setGoalNode(goal)

		self.assertEqual(reporter.countTotalMoves(), 2)

	def test_getMovesInPath(self):
		parent = generateStartNode("C.B...C.BHHHAADD........EEGGGF.....F")
		child = parent.generateChild(getCarFromList("D", parent.cars), 2)
		goal = child.generateChild(getCarFromList("A", child.cars), 4)
		reporter = Reporter(example)
		reporter.setGoalNode(goal)

		self.assertEqual(reporter.getMovesInPath(), ["D right 2", "A right 4"])

	def test_generatePathFromRoot(self):
		parent = generateStartNode("C.B...C.BHHHAADD........EEGGGF.....F")
		child = parent.generateChild(getCarFromList("D", parent.cars), 2)
		goal = child.generateChild(getCarFromList("A", child.cars), 4)
		path = generatePathFromRoot(goal)

		self.assertEqual(path, [parent, child, goal])

	def test_addToSearchPath(self):
		parent = generateStartNode("C.B...C.BHHHAADD........EEGGGF.....F")
		child = parent.generateChild(getCarFromList("D", parent.cars), 2)
		goal = child.generateChild(getCarFromList("A", child.cars), 4)
		reporter = Reporter(example)
		reporter.addToSearchPath(parent, lambda n: 0, lambda n: n.cost(), lambda n: 0)
		reporter.addToSearchPath(child, lambda n: 0, lambda n: n.cost(), lambda n: 0)
		reporter.addToSearchPath(goal, lambda n: 0, lambda n: n.cost(), lambda n: 0)

		expectedSearch1 = "f: 0    g: 0    h: 0    C.B...C.BHHHAADD........EEGGGF.....F"
		expectedSearch2 = "f: 0    g: 1    h: 0    C.B...C.BHHHAA..........EEGGGF.....F"
		expectedSearch3 = "f: 0    g: 2    h: 0    C.B...C.BHHH....AA......EEGGGF.....F"

		self.assertEqual(reporter.searchPath, [expectedSearch1, expectedSearch2, expectedSearch3])

	



if __name__ == '__main__':
    unittest.main()