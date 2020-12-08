inputFilePath = "C:/git-jmschietekat/advent-of-code/2020/day_5_input.txt"


def fileToArr(filePath):
    fileObject = open(filePath, "r")

    arr = []

    for line in fileObject:
        arr.append(line.replace('\n', ''))

    return arr


def split(arr, side):
    half = len(arr) // 2

    if side == 'F' or side == 'L':
        return arr[:half]

    if side == 'B' or side == 'R':
        return arr[half:]


def traverse(seq):
    row_arr = list(range(0, 128))
    column_arr = list(range(0, 8))

    for move in seq[:7]:
        row_arr = split(row_arr, move)

    for move in seq[7:10]:
        column_arr = split(column_arr, move)

    return row_arr[0], column_arr[0], row_arr[0] * 8 + column_arr[0]

def highestSeatId(boardingPasses):
    highestSeatId = 0

    for boardingPass in boardingPasses:
        seatId = traverse(boardingPass)[2]
        if seatId > highestSeatId:
            highestSeatId = seatId

    return highestSeatId

def missingBoardingPass(boardingPasses):
    seatIdArr = []

    for boardingPass in boardingPasses:
        seatIdArr.append(traverse(boardingPass)[2])

    seatIdArr.sort()

    for i, seatId in enumerate(seatIdArr):
        if i > 0:
            if seatIdArr[i] - seatIdArr[i-1] > 1:
                return seatId -1


if __name__ == "__main__":
    boardingPasses = fileToArr(inputFilePath)

    print("Part 1: The highest seat ID on a boarding pass is {}.".format(highestSeatId(boardingPasses)))

    print("Part 2: The missing seat ID is {}.".format(missingBoardingPass(boardingPasses)))

    