import os
from collections import defaultdict, Counter

ROOT_DIR = os.path.dirname(os.path.abspath(__file__)) 
SAMPLE_INPUT_PATH = ROOT_DIR + '\day_06_input_sample.txt'
INPUT_PATH = ROOT_DIR + "\day_06_input.txt"

def calc(arr):
    pass

if __name__ == "__main__":

    print("Sample data")

    arr = [line.replace("\n","").split(" ") for line in open(SAMPLE_INPUT_PATH, "r")]
    print("Part 1 expected answer: {}, calculated answer: {}".format(0, calc(arr)))
    print("Part 2 expected answer: {}, calculated answer: {}".format(0, calc(arr)))

    print("Challange data")

    arr = [line.replace("\n","").split(" ") for line in open(INPUT_PATH, "r")]
    print("Part 1 expected answer: {}, calculated answer: {}".format(0, calc(arr)))
    print("Part 2 expected answer: {}, calculated answer: {}".format(0, calc(arr)))

    