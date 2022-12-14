class PriorityQueue:
	"""
	A data structure acting as a priority queue for the open list.
	It uses a 2D hash table.
	1. The first layer uses the `value` as a key.
	2. The second layer uses the `grid` as a key.
	"""
	def __init__(self, val):
		"""
		`val` us a function that converts the objects in this priority queue into numbers.
		For example, the function can be a heuristic.
		"""
		self.val = val
		self.length = 0
		self.hash = {}
	
	def insert(self, obj:object):
		if self.hash.get(self.val(obj)) is None:
			self.hash[self.val(obj)] = {}
		self.hash[self.val(obj)][str(obj)] = obj
		self.length += 1

	def getMin(self):
		if self.isEmpty():
			return None

		# Finding minimum cost in first layer.
		minVal = None
		for key in self.hash.keys():
			if minVal is None:
				minVal = key
			if key < minVal:
				minVal = key

		# Returning random first value with min cost.
		minHash = self.hash[minVal]
		for min in minHash.values():
			return min

	def removeMin(self):
		if self.isEmpty():
			return None

		min = self.getMin()

		# Removing the value from the secondary hash.
		self.hash[self.val(min)].pop(str(min))

		# Removing the secondary hash if it is empty.
		if len(self.hash[self.val(min)]) == 0:
			self.hash.pop(self.val(min))

		self.length -= 1

		return min

	def getValue(self, obj):
		if self.isEmpty():
			return None

		costHash = self.hash.get(self.val(obj))

		if costHash is None:
			return None

		return costHash.get(str(obj))

	def updateValue(self, obj):
		self.hash[self.val(obj)][str(obj)] = obj

	def isEmpty(self):
		return self.length == 0