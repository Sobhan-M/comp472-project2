import unittest
from position import *

class TestPosition(unittest.TestCase):

	def test_translation1(self):
		position = Position([[1,2], [3,4]])
		position.translate((1,1))
		self.assertEqual(position, Position([[2,3], [4,5]]), "should increase everything by 1")

	def test_translation2(self):
		position = Position([[1,2], [3,4]])
		position.translate((-1,-1))
		self.assertEqual(position, Position([[0,1], [2,3]]), "should decrease everything by 1")

	def test_translation3(self):
		position = Position([[1,2], [3,4]])
		position.translate((0,0))
		self.assertEqual(position, Position([[1,2], [3,4]]), "should change nothing")

	def test_translation4(self):
		position = Position([[1,2], [3,4]])
		position.translate((1,0))
		self.assertEqual(position, Position([[2,2], [4,4]]), "should add to the first value")

	def test_translation5(self):
		position = Position([[1,2], [3,4]])
		position.translate((0,1))
		self.assertEqual(position, Position([[1,3], [3,5]]), "should add to the second value")
	
	def test_copy1(self):
		position1 = Position([[1,2], [3,4]])
		position2 = position1.copy()
		self.assertEqual(position1, position2, "should perfectly copy")

	def test_copy2(self):
		position1 = Position([[1,2], [3,4]])
		position2 = position1.copy()
		position2.translate((1,1))
		self.assertEqual(position1, Position([[1,2], [3,4]]), "should not change original")
		self.assertEqual(position2, Position([[2,3], [4,5]]), "should change copy")

if __name__ == '__main__':
    unittest.main()