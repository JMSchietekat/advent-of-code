inputFilePath = "C:/git-jmschietekat/advent-of-code/2020/day_3_input.txt"


def fileTo2DArr(filePath):
    fileObject = open(filePath, "r")

    arr = []

    for line in fileObject:
        lineArr = []
        for char in line:
            if char == '\n':
                continue
            lineArr.append(char)
        arr.append(lineArr)

    return arr


def traverseAndCount(arr, right, down):
    treeCount = 0
    openSquareCount = 0
    
    height = len(arr)
    width = len(arr[0])

    step = 1   
    for line in arr:
        r = down * step
        c = (right * step) % width
        if down * step < height:
            if arr[r][c] == '.':
                openSquareCount += 1
                # arr[r][c] = '0'
            if arr[r][c] == '#':
                treeCount += 1
                # arr[r][c] = 'X'

            step += 1
        # print(line)

    return treeCount, openSquareCount


if __name__ == "__main__":
    arr = fileTo2DArr(inputFilePath)

    print("Part 1: Traversing right 3 and down 1 would encounter {} trees".format(traverseAndCount(arr, 3, 1)[0]))

    product = traverseAndCount(arr, 1, 1)[0] 
    product *= traverseAndCount(arr, 3, 1)[0] 
    product *= traverseAndCount(arr, 5, 1)[0] 
    product *= traverseAndCount(arr, 7, 1)[0] 
    product *= traverseAndCount(arr, 1, 2)[0] 

    print("Part 2: Traversing product is {}".format(product))
