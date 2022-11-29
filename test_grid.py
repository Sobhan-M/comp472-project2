import unittest
from grid import *
from car import *

example1 = "IIB...C.BHHHC.AAD.....D.EEGGGF.....F"
example2 = "C.B...C.BHHHAADD........EEGGGF.....F"
example3 = "....F...B.F.AABCF....CDD...C....EE.."
example4 = "....F...B.F.AABCF....C.....C....EE.."
example5 = "...................................."
example6 = "..............................AAA..."

class TestGrid(unittest.TestCase):

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
		grid.updateGrid(car, Car(Position([[5,0],[5,1],[5,2]]), 3, "x", "A"))
		self.assertEqual(grid,Grid(".................................AAA"), "should move the As horizontally")

		before = "A.....A............................."
		car = Car(Position([[0,0],[1,0]]),2,"y","A")
		car.move(1)
		grid = Grid(before)
		grid.updateGrid(car, Car(Position([[0,0],[1,0]]),2,"y","A"))
		self.assertEqual(grid, Grid("......A.....A......................."), "should move the As vertically")

	def test_copy(self):
		grid = Grid(example1)
		gridCopy = grid.copy()

		self.assertEqual(grid, gridCopy, "should be equal to copy")
		
		gridCopy.grid[0][0] = "."
		self.assertNotEqual(grid, gridCopy, "should not be affected by change to copy")

	def test_copyMatrix(self):
		m1 = [[1,2,3],[4,5,6]]
		m1Copy = copyMatrix(m1)

		self.assertEqual(m1, m1Copy, "should be equal to copy")

		m1[0][0] = 0
		self.assertNotEqual(m1, m1Copy, "should not be equal to changed copy")

	def test_stringToGrid(self):
		grid3 = [[".", ".", ".", ".", "F", "."],
			[".", ".", "B", ".", "F", "."],
			["A", "A", "B", "C", "F", "."],
			[".", ".", ".", "C", "D", "D"],
			[".", ".", ".", "C", ".", "."],
			[".", ".", "E", "E", ".", "."]]
		self.assertEqual(stringToGrid(example3), grid3)
		
		grid5 = [[".", ".", ".", ".", ".", "."],
			[".", ".", ".", ".", ".", "."],
			[".", ".", ".", ".", ".", "."],
			[".", ".", ".", ".", ".", "."],
			[".", ".", ".", ".", ".", "."],
			[".", ".", ".", ".", ".", "."]]
		self.assertEqual(stringToGrid(example5), grid5)

		grid6 = [[".", ".", ".", ".", ".", "."],
			[".", ".", ".", ".", ".", "."],
			[".", ".", ".", ".", ".", "."],
			[".", ".", ".", ".", ".", "."],
			[".", ".", ".", ".", ".", "."],
			["A", "A", "A", ".", ".", "."]]
		self.assertEqual(stringToGrid(example6), grid6)

	def test_lineString(self):
		grid1 = Grid(example1)
		grid2 = Grid(example2)
		grid3 = Grid(example3)
		grid4 = Grid(example4)

		self.assertEqual(grid1.lineString(), example1)
		self.assertEqual(grid2.lineString(), example2)
		self.assertEqual(grid3.lineString(), example3)
		self.assertEqual(grid4.lineString(), example4)

		


if __name__ == '__main__':
    unittest.main()