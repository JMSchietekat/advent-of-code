import re

inputFilePath = "C:/git-jmschietekat/advent-of-code/2020/day_2_input.txt"


def fileToArr(filePath):
    fileObject = open(filePath, "r")

    lines = []

    for line in fileObject:
        lines.append(line)

    return lines


def strToPolicy(line):
    regex = re.search(r'^(\d*)-(\d*) (\w): (\w*)$', line)

    if(regex):
        return {
            'minCount': int(regex.group(1)),
            'maxCount': int(regex.group(2)),
            'searchChar': regex.group(3),
            'inputStr': regex.group(4)
        }


def isValidPasswordPart1(minCount, maxCount, searchChar, inputStr):

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


def isValidPasswordPart2(minCount, maxCount, searchChar, inputStr):

    if inputStr[minCount-1] == searchChar and inputStr[maxCount-1] != searchChar:
        return True

    if inputStr[minCount-1] != searchChar and inputStr[maxCount-1] == searchChar:
        return True

    return False


if __name__ == "__main__":
    lines = fileToArr(inputFilePath)

    countOfValidPasswords = 0

    for line in lines:
        if isValidPasswordPart1(**strToPolicy(line)) == True:
            countOfValidPasswords += 1

    print('Part 1 has {} valid passwords'.format(countOfValidPasswords))

    countOfValidPasswords = 0

    for line in lines:
        if isValidPasswordPart2(**strToPolicy(line)) == True:
            countOfValidPasswords += 1

    print('Part 2 has {} valid passwords'.format(countOfValidPasswords))
