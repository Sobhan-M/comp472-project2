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

if __name__ == '__main__':
    unittest.main()