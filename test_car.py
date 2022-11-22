import unittest
from position import *
from car import *

class TestCar(unittest.TestCase):

	def test_equal(self):
		car1 = Car(Position([[0,0],[0,1]]), 2, "x", "A")
		car2 = Car(Position([[0,0],[0,1]]), 2, "x", "A")
		car3 = Car(Position([[0,0],[0,2]]), 2, "x", "A")
		car4 = Car(Position([[0,0],[0,1]]), 3, "x", "A")
		car5 = Car(Position([[0,0],[0,1]]), 2, "y", "A")
		car6 = Car(Position([[0,0],[0,1]]), 2, "x", "B")
		# car7 = Car(Position([[0,0],[0,1]]), 2, "x", "A", 99)
		self.assertEqual(car1, car2, "should be equal")
		self.assertNotEqual(car1, car3, "should be unequal because of position")
		self.assertNotEqual(car1, car4, "should be unequal because of length")
		self.assertNotEqual(car1, car5, "should be unequal because of orientation")
		self.assertNotEqual(car1, car6, "should be unequal because of symbol")
		# self.assertNotEqual(car1, car7, "should be unequal because of fuel")

	def test_move(self):
		car = Car(Position([[0,0],[0,1]]), 2, "x", "A", 10)
		car.move(2)
		self.assertEqual(car, Car(Position([[0,2],[0,3]]), 2, "x", "A", 8), "should move right by 2")

		car = Car(Position([[0,0],[0,1]]), 2, "x", "A", 10)
		car.move(-2)
		self.assertEqual(car, Car(Position([[0,-2],[0,-1]]), 2, "x", "A", 8), "should move left by 2")

		car = Car(Position([[0,0],[0,1]]), 2, "y", "A", 10)
		car.move(2)
		self.assertEqual(car, Car(Position([[2,0],[2,1]]), 2, "y", "A", 8), "should move up by 2")

		car = Car(Position([[0,0],[0,1]]), 2, "y", "A", 10)
		car.move(-2)
		self.assertEqual(car, Car(Position([[-2,0],[-2,1]]), 2, "y", "A", 8), "should move down by 2")

		car = Car(Position([[0,0],[0,1]]), 2, "y", "A", 10)
		car.move(1)
		self.assertEqual(car, Car(Position([[1,0],[1,1]]), 2, "y", "A", 9), "should move up by 1")

		car = Car(Position([[0,0],[0,1]]), 2, "y", "A", 10)
		car.move(0)
		self.assertEqual(car, Car(Position([[0,0],[0,1]]), 2, "y", "A", 10), "should not move")

	def test_copy(self):
		car = Car(Position([[0,0],[0,1]]), 2, "x", "A", 10)
		carCopy = car.copy()
		self.assertEqual(car, carCopy, "should be equal")
		self.assertIsNot(car, carCopy, "ensuring this is a different reference")

		carCopy.move(2)
		self.assertEqual(car, Car(Position([[0,0],[0,1]]), 2, "x", "A", 10), "ensuring original does not change")
		self.assertEqual(carCopy, Car(Position([[0,2],[0,3]]), 2, "x", "A", 8), "ensuring new one changes")

	def test_nextPosition(self):
		car = Car(Position([[0,0],[0,1]]), 2, "x", "A", 10)
		pos = car.nextPosition(2)

		self.assertEqual(car, Car(Position([[0,0],[0,1]]), 2, "x", "A", 10), "should not move")
		self.assertEqual(pos, Position([[0,2],[0,3]]), "should be 2 to the right")

		pos = car.nextPosition(-2)
		self.assertEqual(pos, Position([[0,-2],[0,-1]]), "should be 2 to the left")

		car = Car(Position([[0,0],[0,1]]), 2, "y", "A", 10)
		pos = car.nextPosition(1)
		self.assertEqual(pos, Position([[1,0],[1,1]]), "should be 1 up")

		pos = car.nextPosition(-1)
		self.assertEqual(pos, Position([[-1,0],[-1,1]]), "should be 1 down")

		pos = car.nextPosition(0)
		self.assertEqual(pos, Position([[0,0],[0,1]]), "should be the same")

	def test_canUseFuel(self):
		car = Car(Position([[0,0],[0,1]]), 2, "x", "A", 10)

		self.assertTrue(car.canUseFuel(1))
		self.assertTrue(car.canUseFuel(10))
		self.assertFalse(car.canUseFuel(11))
		self.assertFalse(car.canUseFuel(20))

	def test_isAtExit(self):
		car = Car(Position([[2,3],[2,4],[2,5]]), 3, "x", "A", 10)
		self.assertTrue(car.isAtExit())

		car = Car(Position([[2,3],[2,5],[2,4]]), 3, "x", "A", 10)
		self.assertTrue(car.isAtExit())

		car = Car(Position([[2,5],[2,3],[2,4]]), 3, "x", "A", 10)
		self.assertTrue(car.isAtExit())

		car = Car(Position([[2,2],[2,3],[2,4]]), 3, "x", "A", 10)
		self.assertFalse(car.isAtExit())

	def test_findCarSymbols(self):
		
		example1 = "IIB...C.BHHHC.AAD.....D.EEGGGF.....F"
		example2 = "C.B...C.BHHHAADD........EEGGGF.....F"
		example3 = "....F...B.F.AABCF....CDD...C....EE.."
		example4 = "....F...B.F.AABCF....C.....C....EE.."
		example5 = "...................................."
		example6 = "..............................AAA..."

		self.assertEqual(set(findCarSymbols(example1)), {"I", "B", "C", "H", "A", "D", "E", "G", "F"})
		self.assertEqual(set(findCarSymbols(example2)), {"C", "B", "H", "A", "D", "E", "G", "F"})
		self.assertEqual(set(findCarSymbols(example3)), {"F", "B", "A", "C", "D", "E"})
		self.assertEqual(set(findCarSymbols(example4)), {"F", "A", "B", "C", "E"})
		self.assertEqual(set(findCarSymbols(example5)), set([]), "should be empty")
		self.assertEqual(set(findCarSymbols(example6)), {"A"})
		
	def test_findCarPositions(self):
		sample = "B.....B.......................AAA..."
		positions = findCarPositions(sample, ["A", "B"])
		self.assertEqual(Position(positions[0]), Position([[5,0],[5,1],[5,2]]))
		self.assertEqual(Position(positions[1]), Position([[0,0],[1,0]]))
	
	def test_findCarLengths(self):
		sample = "B.....B.......................AAA..."

		lengths1 = findCarLengths1(sample, ["A", "B"])
		lengths2 = findCarLengths2([[[5,0],[5,1],[5,2]], [[0,0],[1,0]]])

		self.assertEqual(lengths1[0], 3, "should be 3 for A")
		self.assertEqual(lengths1[1], 2, "should be 2 for B")

		self.assertEqual(lengths2[0], 3, "should be 3 for A")
		self.assertEqual(lengths2[1], 2, "should be 2 for B")

	def test_findCarOrientation(self):
		orientations = findCarOrientations([[[5,0],[5,1],[5,2]], [[0,0],[1,0]]])

		self.assertEqual(orientations[0], "x", "should be x for A")
		self.assertEqual(orientations[1], "y", "should be y for B")

	def test_generateCarList(self):
		sample = "B.....B.......................AAA..."
		cars = generateCarList(sample)

		if cars[0].symbol == "A":
			self.assertEqual(cars[0], Car(Position([[5,0],[5,1],[5,2]]), 3, "x", "A"), "should be A")
			self.assertEqual(cars[1], Car(Position([[0,0],[1,0]]), 2, "y", "B"), "should be B")
		else:
			self.assertEqual(cars[0], Car(Position([[0,0],[1,0]]), 2, "y", "B"), "should be B")
			self.assertEqual(cars[1], Car(Position([[5,0],[5,1],[5,2]]), 3, "x", "A"), "should be A")


if __name__ == '__main__':
    unittest.main()