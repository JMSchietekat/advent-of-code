from itertools import permutations

inputFilePath = "C:/git-jmschietekat/advent-of-code/2020/day_10_input.txt"


def productOfDelta1AndDelta3(arr):
    delta1 = 0
    delta3 = 0

    for i, e in enumerate(arr):
        if i == 0:
            continue

        if e - arr[i-1] > 3:
            print('Too large difference')

        if e - arr[i-1] == 3:
            delta3 += 1

        if e - arr[i-1] == 1:
            delta1 += 1

    print("Part 1: {} x 1-jolt differences multiplied by {} x 3-jolt differences = {}.".format(delta1, delta3, delta1 * delta3))


def isValid(arr):
    for i, e in enumerate(arr):
        if i == 0:
            continue

        if e - arr[i-1] > 3:
            return False

    # print(arr)
    return True


def tryRemove(arr):
    tempArr = []
    validCount = 1
        
    for i, _ in enumerate(arr):
        tempArr = arr[:]
        if i > 0 and i < len(arr) - 1 :
            tempArr.pop(i)
        else:
            continue

        if isValid(tempArr):
            validCount += 1 + tryRemove(tempArr)
            print(validCount)
            
    return validCount

if __name__ == "__main__":
    arr = [int(line.replace('\n', '')) for line in open(inputFilePath, "r")]

    arr.append(0)
    arr.sort()
    arr.append(arr[-1] + 3)

    productOfDelta1AndDelta3(arr)

    validCount = 0

    validArr = tryRemove(arr)
   

    print(validCount)
