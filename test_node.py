import unittest
from position import *
from car import *
from grid import *
from node import *

example1 = "IIB...C.BHHHC.AAD.....D.EEGGGF.....F"
example2 = "C.B...C.BHHHAADD........EEGGGF.....F"
example3 = "....F...B.F.AABCF....CDD...C....EE.."
example4 = "....F...B.F.AABCF....C.....C....EE.."
example5 = "...................................."
example6 = "..............................AAA..."

class TestNode(unittest.TestCase):

	def test_equal(self):
		node1 = Node(Grid(example6), [Car(Position([[5,0],[5,1],[5,2]]), 3, "x", "A")])
		node2 = Node(Grid(example6), [Car(Position([[5,0],[5,1],[5,2]]), 3, "x", "A")])
		node3 = Node(Grid(example5), [Car(Position([[5,0],[5,1],[5,2]]), 3, "x", "A")])
		node4 = Node(Grid(example6), [Car(Position([[5,1],[5,2],[5,3]]), 3, "x", "A")])
		node5 = Node(Grid(example6), [Car(Position([[5,0],[5,1],[5,2]]), 3, "x", "A")], node4)

		self.assertEqual(node1, node2, "should be equal")
		self.assertNotEqual(node1, node3, "should not be equal because of grid")
		self.assertNotEqual(node1, node4, "should not be equal because of cars")
		self.assertEqual(node1, node5, "should be equal despite parent")

	def test_copy(self):
		node = Node(Grid(example6), [Car(Position([[5,0],[5,1],[5,2]]), 3, "x", "A")])
		nodeCopy = Node(Grid(example6), [Car(Position([[5,0],[5,1],[5,2]]), 3, "x", "A")])

		self.assertEqual(node, nodeCopy, "should match copy")

		nodeCopy.cars[0].symbol = "B"
		self.assertNotEqual(node, nodeCopy, "should not affect original")
		self.assertEqual(node, Node(Grid(example6), [Car(Position([[5,0],[5,1],[5,2]]), 3, "x", "A")]))
		self.assertEqual(nodeCopy, Node(Grid(example6), [Car(Position([[5,0],[5,1],[5,2]]), 3, "x", "B")]))

	def test_isGoal(self):
		car1 = Car(Position([[1,4],[1,5]]), 2, "x", "A") # Not at goal.
		car2 = Car(Position([[1,5],[2,5]]), 2, "y", "A") # At goal.
		car3 = Car(Position([[2,5],[2,4]]), 2, "x", "A") # At goal.
		car4 = Car(Position([[5,0],[5,1]]), 2, "x", "B") # B
		car5 = Car(Position([[2,5],[2,4]]), 2, "x", "B") # B

		self.assertFalse(Node(None, [car1,car4]).isGoal(), "should be false because no one is at output")
		self.assertTrue(Node(None, [car2]).isGoal(), "should be true because A is at output - vertically")
		self.assertTrue(Node(None, [car3]).isGoal(), "should be true because A is at output - horizontally")
		self.assertTrue(Node(None, [car4, car3]).isGoal(), "should be true because A is at output - other car doesn't matter")
		self.assertFalse(Node(None, [car1, car5]).isGoal(), "should be false because B is at output - other car doesn't matter")

	def text_isInBorder(self):
		return

	def test_hasPositionConflict(self):
		return

	def test_canMove(self):
		return
	
	def test_copyCarsList(self):
		return

	def test_generateChild(self):
		# Test if new node has the right grid and car.
		# Test if parent is correct.
		# Test if children are correct.
		return

	def test_expandChildren(self):
		return

	def test_isRoot(self):
		parent = Node(None, [])
		child = Node(None, [], parent)

		self.assertTrue(parent.isRoot())
		self.assertFalse(child.isRoot())

	def test_cost(self):
		parent = Node(None, [])
		child = Node(None, [], parent)
		grandChild = Node(None, [], child)
		greatGrandChild = Node(None, [], grandChild)

		self.assertEqual(parent.cost(), 0, "root should have no cost")
		self.assertEqual(child.cost(), 1)
		self.assertEqual(grandChild.cost(), 2)
		self.assertEqual(greatGrandChild.cost(), 3)
	


if __name__ == '__main__':
    unittest.main()