inputFilePath = "C:/git-jmschietekat/advent-of-code/2020/day_1_input.txt"

def fileToArr(filePath):
	fileObject = open(filePath, "r")

	intArr = []

	for line in fileObject:
		intArr.append(int(line))

	return intArr

def productOfTwoValuesThatSumTo2020(inputArr = []):
	for i, a in enumerate(inputArr):
		for j, b in enumerate(inputArr):
			if i == j: continue

			if a + b == 2020:
				return a * b

	return None

print("Answer to part 1: ", productOfTwoValuesThatSumTo2020(fileToArr(inputFilePath)))

def productOfThreeValuesThatSumTo2020(inputArr = []):
	for i, a in enumerate(inputArr):
		for j, b in enumerate(inputArr):
			for k, c in enumerate(inputArr):
				if i == j or j == k or k == i: continue

				if a + b + c == 2020:
					return a * b * c

	return None

print("Answer to part 2: ", productOfThreeValuesThatSumTo2020(fileToArr(inputFilePath)))