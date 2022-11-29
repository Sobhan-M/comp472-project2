from randompuzzle import *
import unittest

class TestRandomPuzzle(unittest.TestCase):
	def test_findAllInstances(self):
		self.assertEqual(findAllInstances("......", ".."), [0,1,2,3,4])
		self.assertEqual(findAllInstances("AAAAAA", "."), [])
		self.assertEqual(findAllInstances("A.A...", ".."), [3,4])
		self.assertEqual(findAllInstances("A.A..A", ".."), [3])
		self.assertEqual(findAllInstances("A....A", ".."), [1,2,3])
		self.assertEqual(findAllInstances("A.A.A.", ".."), [])
		self.assertEqual(findAllInstances("A...A.", "..."), [1])

	def test_addCarToVector(self):
		vector = [".", ".", ".", ".", ".", "."]
		car = "A"
		result = addCarToVector(vector, car, 3)
		self.assertEqual(result, vector)

		vector2 = ["A", "A", ".", ".", "C", "."]
		car2 = "B"
		result2 = addCarToVector(vector2, car2, 2)
		self.assertEqual(result2, ["A", "A", "B", "B", "C", "."])

		vector3 = ["B", ".", ".", ".", "C", "."]
		car3 = "A"
		result3 = addCarToVector(vector3, car3, 3)
		self.assertEqual(result3, ["B", "A", "A", "A", "C", "."])

		vector4 = ["B", "B", ".", ".", "C", "."]
		car4 = "D"
		result4 = addCarToVector(vector4, car4, 3)
		self.assertIsNone(result4)



if __name__ == '__main__':
    unittest.main()