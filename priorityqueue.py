class PriorityQueue:
	def __init__(self, val):
		"""
		`val` us a function that converts the objects in this priority queue into numbers.
		For example, the function can be a heuristic.
		Uses a 2D hash table. First layer is the cost. Second layer is a string representation of the node.
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

	def isEmpty(self):
		return self.length == 0