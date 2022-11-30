def extractPuzzleLines(fileName:str):
	"""
	Returns a list of puzzles from a given file.
	- Ignores empty lines.
	- Ignores lines starting with #
	"""
	puzzleLines = list()
	with open(fileName, "r") as file:
		for line in file:
			if line.isspace() or line[0] == "#":
				continue
			endOfLineIndex = line.find("\n")
			if endOfLineIndex == -1:
				puzzleLines.append(line)
			else:
				puzzleLines.append(line[:endOfLineIndex])
	return puzzleLines

def getGrid(puzzleLine:str):
	"""
	Gets the grid string from a puzzle line.
	"""
	return puzzleLine.split(" ")[0]

def getFuel(puzzleLine:str):
	"""
	Returns a `dict` of fuel corresponding to each car.
	"""
	allCarsFuel = dict()
	splitLine = puzzleLine.split(" ")
	if len(splitLine) == 1:
		return allCarsFuel
	for carsFuel in splitLine[1:]:
		if carsFuel.isspace() or carsFuel == "":
			continue
		allCarsFuel[carsFuel[0]] = int(carsFuel[1:])
	return allCarsFuel
	
			