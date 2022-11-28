import unittest

from grid import *
from node import *
from heuristics import *

example1 = "IIB...C.BHHHC.AAD.....D.EEGGGF.....F"
example2 = "C.B...C.BHHHAADD........EEGGGF.....F"
example3 = "...GF...BGF.AABCF....CDD...C....EE.."
example4 = "....F...B.F.AABCF....C.....C....EE.."

class TestHeuristic(unittest.TestCase):
	def test_h1(self):
		node1 = generateStartNode(example1)
		node2 = generateStartNode(example2)
		node3 = generateStartNode(example3)
		node4 = generateStartNode(example4)

		self.assertEqual(h1(node1), 1)
		self.assertEqual(h1(node2), 1)
		self.assertEqual(h1(node3), 3)
		self.assertEqual(h1(node4), 3)

	def test_h2(self):
		node1 = generateStartNode(example1)
		node2 = generateStartNode(example2)
		node3 = generateStartNode(example3)
		node4 = generateStartNode(example4)

		self.assertEqual(h2(node1), 1)
		self.assertEqual(h2(node2), 2)
		self.assertEqual(h2(node3), 3)
		self.assertEqual(h2(node4), 3)

	def test_h3(self):
		node1 = generateStartNode(example1)
		node2 = generateStartNode(example2)
		node3 = generateStartNode(example3)
		node4 = generateStartNode(example4)

		self.assertEqual(h3(node1, 2), 2)
		self.assertEqual(h3(node2, 2), 2)
		self.assertEqual(h3(node3, 2), 6)
		self.assertEqual(h3(node4, 2), 6)

	def test_h4(self):
		node1 = generateStartNode(example1)
		node2 = generateStartNode(example2)
		node3 = generateStartNode(example3)
		node4 = generateStartNode(example4)

		self.assertEqual(h4(node1), 0.5)
		self.assertEqual(h4(node2), 1)
		self.assertEqual(h4(node3), 1)
		self.assertEqual(h4(node4), 1)
	
	def test_h5(self):
		node1 = generateStartNode(example1)
		node2 = generateStartNode(example2)
		node3 = generateStartNode(example3)
		node4 = generateStartNode(example4)

		self.assertEqual(h5(node1), 1.5)
		self.assertEqual(h5(node2), 2)
		self.assertEqual(h5(node3), 4)
		self.assertEqual(h5(node4), 4)



if __name__ == '__main__':
    unittest.main()