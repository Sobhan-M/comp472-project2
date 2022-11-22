def extractPuzzleLines(fileName:str):
	puzzleLines = list()
	with open(fileName, "r") as file:
		for line in file:
			if line[0:1] ==  "\n" or line[0] == "#":
				continue
			endOfLineIndex = line.find("\n")
			if endOfLineIndex == -1:
				puzzleLines.append(line)
			else:
				puzzleLines.append(line[:endOfLineIndex])
	return puzzleLines

def getGrid(puzzleLine:str):
	return puzzleLine.split(" ")[0]

def getFuel(puzzleLine:str):
	allCarsFuel = dict()
	splitLine = puzzleLine.split(" ")
	if len(splitLine) == 1:
		return allCarsFuel
	for carsFuel in splitLine[1:]:
		allCarsFuel[carsFuel[0]] = int(carsFuel[1:])
	return allCarsFuel
	
			