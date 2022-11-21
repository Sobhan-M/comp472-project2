import unittest
from priorityqueue import *

class TestPriorityQueue(unittest.TestCase):
	def test_insert(self):
		pq = PriorityQueue(lambda x: x) # Value is the same as the object.
		pq.insert(1)
		pq.insert(2)
		pq.insert(3)

		self.assertEqual(len(pq.array), 3)
		self.assertEqual(pq.array, [1,2,3])

	def test_insertList(self):
		pq = PriorityQueue(lambda x: x) # Value is the same as the object.
		pq.insertList([1,2,3])

		self.assertEqual(len(pq.array), 3)
		self.assertEqual(pq.array, [1,2,3])

	def test_getMin(self):
		pq = PriorityQueue(lambda x: x) # Value is the same as the object.
		pq.insert(3)
		pq.insert(2)
		pq.insert(1)

		self.assertEqual(pq.getMin(), 1)
		self.assertEqual(pq.array, [3,2,1])

		pq = PriorityQueue(lambda x: -x) # Returns max this time.
		pq.insert(3)
		pq.insert(2)
		pq.insert(1)

		self.assertEqual(pq.getMin(), 3)
		self.assertEqual(pq.array, [3,2,1])

		pq = PriorityQueue(lambda x: -(x % 3))
		pq.insert(3)
		pq.insert(2)
		pq.insert(1)

		self.assertEqual(pq.getMin(), 2)
		self.assertEqual(pq.array, [3,2,1])

	def test_removeMin(self):
		pq = PriorityQueue(lambda x: x) # Value is the same as the object.
		pq.insert(3)
		pq.insert(2)
		pq.insert(1)

		self.assertEqual(pq.removeMin(), 1)
		self.assertEqual(pq.array, [3,2])

		pq = PriorityQueue(lambda x: -x) # Returns max this time.
		pq.insert(3)
		pq.insert(2)
		pq.insert(1)

		self.assertEqual(pq.removeMin(), 3)
		self.assertEqual(pq.array, [2,1])

		pq = PriorityQueue(lambda x: -(x % 3))
		pq.insert(3)
		pq.insert(2)
		pq.insert(1)

		self.assertEqual(pq.removeMin(), 2)
		self.assertEqual(pq.array, [3,1])

	def test_isEmpty(self):
		pq = PriorityQueue(lambda x: x) # Value is the same as the object.
		pq.insert(3)
		pq.insert(2)
		pq.insert(1)

		self.assertFalse(pq.isEmpty())
		pq.removeMin()
		self.assertFalse(pq.isEmpty())
		pq.removeMin()
		self.assertFalse(pq.isEmpty())
		pq.removeMin()
		self.assertTrue(pq.isEmpty())

	def test_isInList(self):
		pq = PriorityQueue(lambda x: x) # Value is the same as the object.
		pq.insert(3)
		pq.insert(2)
		pq.insert(1)

		self.assertFalse(isInList(5, pq.array))
		self.assertTrue(isInList(1, pq.array))
		self.assertTrue(isInList(2, pq.array))
		self.assertTrue(isInList(3, pq.array))

	def test_findIndex(self):
		pq = PriorityQueue(lambda x: x) # Value is the same as the object.

		self.assertEqual(pq.findIndex(1), -1)
		pq.insert(3)
		pq.insert(2)
		pq.insert(1)
		self.assertEqual(pq.findIndex(1), 2)
		self.assertEqual(pq.findIndex(2), 1)
		self.assertEqual(pq.findIndex(3), 0)
		self.assertEqual(pq.findIndex(4), -1)


if __name__ == '__main__':
    unittest.main()