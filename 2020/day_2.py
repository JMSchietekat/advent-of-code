import re

inputFilePath = "C:/git-jmschietekat/advent-of-code/2020/day_2_input.txt"

def fileToArr(filePath):
    fileObject = open(filePath, "r")

    lines = []

    for line in fileObject:
        lines.append(line)

    return lines

def isValid(line):
    regex = re.search(r'^(\d*)-(\d*) (\w): (\w*)$', line)

    if(regex):
        minCount = int(regex.group(1))
        maxCount = int(regex.group(2))
        searchChar = regex.group(3)
        inputStr = regex.group(4)

        charCount = 0

        for char in inputStr:
            if char == searchChar:
                charCount += 1
            if charCount > maxCount:
                return False

        if charCount < minCount:
            return False
        else:
            return True
        
    else:
        return False


if __name__ == "__main__":
    lines = fileToArr(inputFilePath)

    countOfValidPasswords = 0

    for line in lines:
        if isValid(line) == True:
            countOfValidPasswords += 1

    print(countOfValidPasswords)
