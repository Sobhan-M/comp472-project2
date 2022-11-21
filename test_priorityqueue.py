import unittest
from priorityqueue import *

class TestPriorityQueue(unittest.TestCase):
	def test_insert(self):
		pq = PriorityQueue(lambda x: x) # Value is the same as the object.
		pq.insert(1)
		pq.insert(2)
		pq.insert(3)

		self.assertEqual(pq.length, 3)

	def test_getMin(self):
		pq = PriorityQueue(lambda x: x) # Value is the same as the object.
		pq.insert(3)
		pq.insert(2)
		pq.insert(1)

		self.assertEqual(pq.getMin(), 1)
		self.assertEqual(pq.length, 3)

		pq = PriorityQueue(lambda x: -x) # Returns max this time.
		pq.insert(3)
		pq.insert(2)
		pq.insert(1)

		self.assertEqual(pq.getMin(), 3)
		self.assertEqual(pq.length, 3)

		pq = PriorityQueue(lambda x: -(x % 3))
		pq.insert(3)
		pq.insert(2)
		pq.insert(1)

		self.assertEqual(pq.getMin(), 2)
		self.assertEqual(pq.length, 3)

	def test_removeMin(self):
		pq = PriorityQueue(lambda x: x) # Value is the same as the object.
		pq.insert(3)
		pq.insert(2)
		pq.insert(1)

		self.assertEqual(pq.removeMin(), 1)
		self.assertEqual(pq.length, 2)

		pq = PriorityQueue(lambda x: -x) # Returns max this time.
		pq.insert(3)
		pq.insert(2)
		pq.insert(1)

		self.assertEqual(pq.removeMin(), 3)
		self.assertEqual(pq.length, 2)

		pq = PriorityQueue(lambda x: -(x % 3))
		pq.insert(3)
		pq.insert(2)
		pq.insert(1)

		self.assertEqual(pq.removeMin(), 2)
		self.assertEqual(pq.length, 2)

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


if __name__ == '__main__':
    unittest.main()