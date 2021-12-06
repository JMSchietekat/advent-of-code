import os
from collections import defaultdict, Counter

ROOT_DIR = os.path.dirname(os.path.abspath(__file__)) 
SAMPLE_INPUT_PATH = ROOT_DIR + '\day_6_input_sample.txt'
INPUT_PATH = ROOT_DIR + "\day_6_input.txt"

def calc(initial_state, days):
    I = initial_state
    for _ in range(days):
        A = defaultdict(int)
        for val, cnt in I.items():
            if val==0:
                A[6] += cnt
                A[8] += cnt
            else:
                A[val-1] += cnt
        I = A
    return sum(I.values())

def process_input(input_path):       
    return Counter([int(v) for v in open(input_path).read().strip().split(',')])

if __name__ == "__main__":

    print("Sample data")

    initial_state = process_input(SAMPLE_INPUT_PATH)
    print("Part 1 expected answer: {}, calculated answer: {}".format(26, calc(initial_state, 18)))
    print("Part 1 expected answer: {}, calculated answer: {}".format(5934, calc(initial_state, 80)))
    print("Part 2 expected answer: {}, calculated answer: {}".format(26984457539, calc(initial_state, 256)))

    print("Challange data")

    initial_state = process_input(INPUT_PATH)
    print("Part 1 expected answer: {}, calculated answer: {}".format(391888, calc(initial_state,80)))
    print("Part 2 expected answer: {}, calculated answer: {}".format(1754597645339, calc(initial_state,256)))

    