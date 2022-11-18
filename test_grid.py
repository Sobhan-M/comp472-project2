import unittest
from grid import *
from car import *

example1 = "IIB...C.BHHHC.AAD.....D.EEGGGF.....F"
example2 = "C.B...C.BHHHAADD........EEGGGF.....F"
example3 = "....F...B.F.AABCF....CDD...C....EE.."
example4 = "....F...B.F.AABCF....C.....C....EE.."
example5 = "...................................."
example6 = "..............................AAA..."

class TestPosition(unittest.TestCase):

	def test_equal(self):
		
		self.assertEqual(Grid(example1), Grid(example1), "should be equal")
		self.assertNotEqual(Grid(example1), Grid(example2), "should not be equal")

		grid = [[".", ".", ".", ".", ".", "."],
			[".", ".", ".", ".", ".", "."],
			[".", ".", ".", ".", ".", "."],
			[".", ".", ".", ".", ".", "."],
			[".", ".", ".", ".", ".", "."],
			[".", ".", ".", ".", ".", "."]]
		
		self.assertEqual(Grid(example5), Grid(grid), "should be equal")

	def test_updateGrid(self):
		grid = Grid(example6)
		car = Car(Position([[5,3],[5,4],[5,5]]), 3, "x", "A")
		grid.updateGrid(car)
		self.assertEqual(grid,Grid(".................................AAA"), "should move the As horizontally")

		before = "A.....A............................."
		car = Car(Position([[0,0],[1,0]]),2,"y","A")
		car.move(1)
		grid = Grid(before)
		grid.updateGrid(car)
		self.assertEqual(grid, Grid("......A.....A......................."), "should move the As vertically")

	def test_copy(self):
		grid = Grid(example1)
		gridCopy = grid.copy()

		self.assertEqual(grid, gridCopy, "should be equal to copy")
		
		gridCopy.grid[0][0] = "."
		self.assertNotEqual(grid, gridCopy, "should not be affected by change to copy")


if __name__ == '__main__':
    unittest.main()