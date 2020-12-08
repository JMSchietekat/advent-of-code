inputFilePath = "C:/git-jmschietekat/advent-of-code/2020/day_6_input.txt"

def fileToArr(filePath):
    fileObject = open(filePath, "r")

    arr = []

    tempLine = ''

    for line in fileObject:
        tempLine += line.replace('\n', '')

        if line == '\n':
            arr.append(tempLine)
            tempLine = ''

    arr.append(tempLine)

    return arr

def score(answers):    
    arr = sorted(answers)
    score = 1

    for i, _ in enumerate(arr):
        if i > 0:
            if arr[i] != arr[i-1]:
                score += 1

    return score
            

if __name__ == "__main__":
    arr = fileToArr(inputFilePath)

    totalScore = 0

    for line in arr:
        totalScore += score(line)

    print("Part 1: The total score is {}.".format(totalScore))

    