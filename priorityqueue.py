class PriorityQueue:
	def __init__(self, val):
		"""
		`val` us a function that converts the objects in this priority queue into numbers.
		For example, the function can be a heuristic.
		"""
		self.val = val
		self.array = []
	
	def insert(self, obj:object):
		self.array.append(obj)

	def insertList(self, objList:list):
		for obj in objList:
			self.array.append(obj)

	def getMin(self):
		if len(self.array) == 0:
			return None

		minIndex = 0
		min = self.array[0]
		minValue = self.val(min)

		for i in range(len(self.array)):
			if self.val(self.array[i]) < minValue:
				minIndex = i
				min = self.array[minIndex]
				minValue = self.val(min)

		return min

	def removeMin(self):
		if len(self.array) == 0:
			return None
		
		minIndex = 0
		min = self.array[0]
		minValue = self.val(min)

		for i in range(len(self.array)):
			if self.val(self.array[i]) < minValue:
				minIndex = i
				min = self.array[minIndex]
				minValue = self.val(min)

		self.array.pop(minIndex)

		return min

	def isEmpty(self):
		return len(self.array) == 0
		
def isInList(obj, array):
	for element in array:
		if obj == element:
			return True
	return False