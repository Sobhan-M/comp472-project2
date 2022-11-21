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

	def test_isInBorder(self):
		self.assertTrue(isInBorder(Position([[0,0]])))
		self.assertFalse(isInBorder(Position([[6,0]])))
		self.assertFalse(isInBorder(Position([[-6,0]])))
		self.assertFalse(isInBorder(Position([[0,6]])))
		self.assertFalse(isInBorder(Position([[0,-6]])))
		self.assertTrue(isInBorder(Position([[0,0], [0,1], [0,2]])))
		self.assertFalse(isInBorder(Position([[0,0], [0,-1], [0,-2]])))

	def test_hasPositionConflict(self):
		car1 = Car(Position([[0,0],[0,1],[0,2]]), 3, "x", "A")
		car2 = Car(Position([[0,3],[0,4],[0,5]]), 3, "x", "B")
		car3 = Car(Position([[1,0],[2,0],[3,0]]), 3, "y", "C")
		car4 = Car(Position([[5,0],[5,1],[5,2]]), 3, "x", "D")
		car5 = Car(Position([[2,3],[3,3],[4,3]]), 3, "y", "E")

		self.assertFalse(hasPositionConflict([car1,car2,car3,car4,car5], car1.symbol, car1.positions))
		self.assertFalse(hasPositionConflict([car1,car2,car3,car4,car5], car2.symbol, car2.positions))
		self.assertFalse(hasPositionConflict([car1,car2,car3,car4,car5], car3.symbol, car3.positions))
		self.assertFalse(hasPositionConflict([car1,car2,car3,car4,car5], car4.symbol, car4.positions))
		self.assertFalse(hasPositionConflict([car1,car2,car3,car4,car5], car5.symbol, car5.positions))
		self.assertTrue(hasPositionConflict([car1,car2,car3,car4,car5], car1.symbol, car1.nextPosition(1)))
		self.assertTrue(hasPositionConflict([car1,car2,car3,car4,car5], car2.symbol, car2.nextPosition(-1)))
		self.assertTrue(hasPositionConflict([car1,car2,car3,car4,car5], car3.symbol, car3.nextPosition(-1)))
		self.assertFalse(hasPositionConflict([car1,car2,car3,car4,car5], car3.symbol, car3.nextPosition(1)))
		self.assertTrue(hasPositionConflict([car1,car2,car3,car4,car5], car3.symbol, car3.nextPosition(2)))
		self.assertFalse(hasPositionConflict([car1,car2,car3,car4,car5], car5.symbol, car5.nextPosition(-1)))
		self.assertTrue(hasPositionConflict([car1,car2,car3,car4,car5], car5.symbol, car5.nextPosition(-2)))

	def test_canMove(self):
		carA = Car(Position([[2,0],[2,1]]), 2, "x", "A")
		carB = Car(Position([[1,2],[2,2]]), 2, "y", "B", 2)

		self.assertTrue(canMove(carA, 0, [carA, carB]))
		self.assertFalse(canMove(carA, 1, [carA, carB]), "should intersect with B")
		self.assertFalse(canMove(carA, -1, [carA, carB]), "should leave area")
		self.assertFalse(canMove(carB, 3, [carA, carB]), "should run out of fuel")
		self.assertFalse(canMove(carA, 3, [carA, carB]))

	
	def test_copyCarsList(self):
		carA = Car(Position([[2,0],[2,1]]), 2, "x", "A")
		carB = Car(Position([[1,2],[2,2]]), 2, "y", "B", 2)
		copies = copyCarsList([carA, carB])

		self.assertTrue(carA == copies[0])
		self.assertTrue(carB == copies[1])
		copies[0].move(1)
		self.assertFalse(carA == copies[0], "should not affect the original")

	def test_moveFromParent(self):
		carA = Car(Position([[2,0],[2,1]]), 2, "x", "A")
		carB = Car(Position([[1,2],[2,2]]), 2, "y", "B", 2)

		self.assertEqual(moveFromParent(carA, 2), "A right 2")
		self.assertEqual(moveFromParent(carA, -3), "A left 3")
		self.assertEqual(moveFromParent(carB, 1), "B down 1")
		self.assertEqual(moveFromParent(carB, -2), "B up 2")
		self.assertRaises(Exception, moveFromParent(carB, 0), "should raise exception")

	def test_generateChild(self):
		carA = Car(Position([[2,0],[2,1]]), 2, "x", "A")
		carB = Car(Position([[1,2],[2,2]]), 2, "y", "B", 2)
		grid = "........B...AAB....................."
		parent = Node(Grid(grid), [carA,carB], None, [])

		child1 = parent.generateChild(carA, 1)
		self.assertIsNone(child1, "should not be a valid child or move")

		child2 = parent.generateChild(carB, 1)
		self.assertEqual(child2.grid, Grid("............AAB.....B..............."))

		self.assertEqual(child2.cars[0], carA)
		self.assertEqual(child2.cars[1], Car(Position([[2,2],[3,2]]), 2, "y", "B", 1))

		self.assertIs(child2.parent, parent)
		self.assertIs(parent.children[0], child2)
		
	def test_expandChildren(self):
		car = Car(Position([[2,0],[2,1]]), 2, "x", "A")
		grid = "............AA......................"
		node = Node(Grid(grid), [car])
		children = node.expandChildren()

		self.assertEqual(len(children), 4)
		self.assertTrue(children[0].isGoal())

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