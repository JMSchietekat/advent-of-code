inputFilePath = "C:/git-jmschietekat/advent-of-code/2020/day_9_input.txt"


def fileToArr(filePath):
    fileObject = open(filePath, "r")

    arr = []

    for line in fileObject:
        arr.append(int(line))

    return arr

def isValid(buffer, val):
    for ia, va in enumerate(buffer):
        for ib, vb in enumerate(buffer):
            if ia != ib:
                if va + vb == val:
                    buffer.append(val)
                    buffer.pop(0)
                    return buffer

    return [val]

if __name__ == "__main__":
    arr = fileToArr(inputFilePath)

    preamableSize = 25

    preamable = arr[:preamableSize]
    stream = arr[preamableSize:]

    buffer = isValid(preamable, stream[0])
    cnt = 1

    while len(buffer) > 1:
        buffer = isValid(preamable, stream[cnt])
        cnt += 1

    print(buffer)

    