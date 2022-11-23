from node import *
from grid import *

def h1(node:Node):
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
	return k * h1(node)