inputFilePath = "C:/git-jmschietekat/advent-of-code/2020/day_6_input.txt"

def fileToArr(filePath):
    fileObject = open(filePath, "r")

    arr = []

    tempLine = ''

    for line in fileObject:
        if line == '\n':
            arr.append(tempLine[:-1])
            tempLine = ''
            continue

        tempLine += line.replace('\n', ',')

    arr.append(tempLine[:-1])

    return arr

def find_similarity(string_a, string_b):
    returnStr = ''
    for ca in string_a:
        for cb in string_b:
            if ca == cb:
                returnStr += ca
    return returnStr

def score(answers): 
    groups = answers.split(',') 

    if len(groups) == 1:
        return len(groups[0])

    yieldStr = find_similarity(groups[0], groups[1])

    for i in range(1,len(groups)):
        yieldStr = find_similarity(yieldStr, groups[i])

    return len(yieldStr)

            

if __name__ == "__main__":
    arr = fileToArr(inputFilePath)

    totalScore = 0

    for line in arr:
        totalScore += score(line)

    print("Part 2: The total score is {}.".format(totalScore))

    