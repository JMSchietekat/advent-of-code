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


if __name__ == "__main__":
    arr = fileToArr(inputFilePath)

    highest_seat_id = 0

    for boardingPass in arr:
        seat_id = traverse(boardingPass)[2]
        if seat_id > highest_seat_id:
            highest_seat_id = seat_id

    print("Part 1: The highest seat ID on a boarding pass is {}.".format(highest_seat_id))