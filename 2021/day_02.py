import os

ROOT_DIR = os.path.dirname(os.path.abspath(__file__)) 
SAMPLE_INPUT_PATH = ROOT_DIR + '\day_02_input_sample.txt'
INPUT_PATH = ROOT_DIR + "\day_02_input.txt"

def calculate(arr):
    coord = [0, 0]

    for move in arr:
        if move[0] == "forward":
            coord[0] += int(move[1])
        if move[0] == "up":
            coord[1] -= int(move[1])
        if move[0] == "down":
            coord[1] += int(move[1])

    return coord[0] * coord[1]

def calculate2(arr):
    coord = [0, 0, 0]

    for move in arr:
        if move[0] == "forward":
            coord[0] += int(move[1])
            coord[1] += int(move[1])*coord[2]
        if move[0] == "up":
            coord[2] -= int(move[1])
        if move[0] == "down":
            coord[2] += int(move[1])

    return coord[0] * coord[1]


if __name__ == "__main__":
    arr = [line.replace("\n","").split(" ") for line in open(SAMPLE_INPUT_PATH, "r")]

    print("Sample data")
    print("Part 1 expected answer: {}, calculated answer: {}".format(150, calculate(arr)))
    print("Part 2 expected answer: {}, calculated answer: {}".format(900, calculate2(arr)))

    arr = [line.replace("\n","").split(" ") for line in open(INPUT_PATH, "r")]

    print("Challange data")
    print("Part 1 expected answer: {}, calculated answer: {}".format(2272262, calculate(arr)))
    print("Part 2 expected answer: {}, calculated answer: {}".format(2134882034, calculate2(arr)))

    