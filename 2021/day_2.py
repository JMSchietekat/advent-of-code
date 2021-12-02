sample_input_file_path = "C:/git-jmschietekat/advent-of-code/2021/day_2_input_sample.txt"
input_file_path = "C:/git-jmschietekat/advent-of-code/2021/day_2_input.txt"

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
    arr = [line.replace("\n","").split(" ") for line in open(sample_input_file_path, "r")]

    print("Sample data")
    print("Part 1 expected answer: {}, calculated answer: {}".format(150, calculate(arr)))
    print("Part 2 expected answer: {}, calculated answer: {}".format(900, calculate2(arr)))

    arr = [line.replace("\n","").split(" ") for line in open(input_file_path, "r")]

    print("Challange data")
    print("Part 1 expected answer: {}, calculated answer: {}".format(2272262, calculate(arr)))
    print("Part 2 expected answer: {}, calculated answer: {}".format(2134882034, calculate2(arr)))

    