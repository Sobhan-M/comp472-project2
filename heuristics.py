from node import *
from grid import *

def h1(node:Node):
	"""
	Counts the number of blocking vehicles in front of A.
	"""
	row = node.grid.grid[2]
	numOfCars = 0
	carsSeen = dict()

	for block in reversed(row):
		if block == "A":
			break
		if block == ".":
			continue
		car = carsSeen.get(block)
		if car is None:
			numOfCars += 1
			carsSeen[block] = block

	return numOfCars

def h2(node:Node):
	"""
	Counts the number of blocked positions in front of A.
	"""
	row = node.grid.grid[2]
	numOfBlocked = 0

	for block in reversed(row):
		if block == "A":
			break
		if block == ".":
			continue
		numOfBlocked += 1

	return numOfBlocked

def h3(node:Node, k=2):
	"""
	Is `h2` times constant `k`.
	"""
	return k * h1(node)

def h4(node:Node):
	"""
	Counts the blocks to the goal divided by 4.
	"""
	row = node.grid.grid[2]
	numOfBlocks = 0
	
	for block in reversed(row):
		if block == "A":
			break
		numOfBlocks += 1
	
	return numOfBlocks/4

def h5(node:Node):
	"""
	A combination of `h1` and `h4`.
	"""
	return h1(node) + h4(node)