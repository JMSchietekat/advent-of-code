import os

ROOT_DIR = os.path.dirname(os.path.abspath(__file__)) 
SAMPLE_INPUT_PATH = ROOT_DIR + '\day_3_input_sample.txt'
INPUT_PATH = ROOT_DIR + "\day_3_input.txt"

def day3(arr):
    pass


if __name__ == "__main__":
    arr = [line.replace("\n","").split(" ") for line in open(SAMPLE_INPUT_PATH, "r")]

    print("Sample data")
    print("Part 1 expected answer: {}, calculated answer: {}".format("?", day3(arr)))
    print("Part 2 expected answer: {}, calculated answer: {}".format("?", day3(arr)))

    arr = [line.replace("\n","").split(" ") for line in open(INPUT_PATH, "r")]

    print("Challange data")
    print("Part 1 expected answer: {}, calculated answer: {}".format("?", day3(arr)))
    print("Part 2 expected answer: {}, calculated answer: {}".format("?", day3(arr)))

    