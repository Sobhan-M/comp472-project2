class PriorityQueue:
	def __init__(self, val):
		"""
		`val` us a function that converts the objects in this priority queue into numbers.
		For example, the function can be a heuristic.
		"""
		self.val = val
		self.hash = {}
	
	def insert(self, obj:object):
		self.hash[str(obj)] = obj

	def getMin(self):
		if len(self.hash) == 0:
			return None

		min = None

		for value in self.hash.values():
			if min is None:
				min = value

			if self.val(value) < self.val(min):
				min = value
		
		return min

	def removeMin(self):
		min = self.getMin()
		self.hash.pop(str(min))
		return min

	def isEmpty(self):
		return len(self.hash) == 0