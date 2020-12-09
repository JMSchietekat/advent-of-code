inputFilePath = "C:/git-jmschietekat/advent-of-code/2020/day_9_input.txt"

def fileToArr(filePath):
    fileObject = open(filePath, "r")

    arr = []

    for line in fileObject:
        arr.append(int(line))

    return arr

def checkValue(buffer, val):
    for ia, va in enumerate(buffer):
        for ib, vb in enumerate(buffer):
            if ia != ib:
                if va + vb == val:
                    buffer.append(val)
                    buffer.pop(0)
                    return buffer # return buffer if valid

    return [val] # return value is invalid

def searchForEncryptionWeakness(arr, invalidValue):
    tempBuffer = []
    tempTotal = 0

    for ia, va in enumerate(arr):
        tempBuffer.append(va)
        tempTotal = va
        for vb in arr[ia+1:]:
            tempBuffer.append(vb)
            tempTotal += vb
            if tempTotal > invalidValue:
                tempBuffer = []
                tempTotal = 0
                break

            if tempTotal == invalidValue:
                tempBuffer.sort()
                return tempBuffer[0] + tempBuffer[-1]


def getInvalidValue(arr):
    preamableSize = 25

    preamable = arr[:preamableSize]
    stream = arr[preamableSize:]

    buffer = checkValue(preamable, stream[0])
    cnt = 1

    while len(buffer) > 1:
        buffer = checkValue(preamable, stream[cnt])
        cnt += 1

    return buffer[0]

if __name__ == "__main__":
    arr = fileToArr(inputFilePath)

    invalidValue = getInvalidValue(arr)

    print("Part 1: The invalid value is {}.".format(invalidValue))

    print("Part 2: The encryption weakness value is {}.".format(searchForEncryptionWeakness(arr, invalidValue)))

    

    