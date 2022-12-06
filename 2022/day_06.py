import os
from collections import Counter

ROOT_DIR = os.path.dirname(os.path.abspath(__file__)) 
SAMPLE_INPUT_PATH = ROOT_DIR + '/day_06_input_sample.txt'
INPUT_PATH = ROOT_DIR + "/day_06_input.txt"

def p1(path):
    l = open(path, "r").read().strip()

    S = []
    for i, c in enumerate(l):
        S.append(c)
        if len(S) >= 4: 
            if len(Counter("".join(S))) == len("".join(S)):
                return i + 1
            S.pop(0)

def p2(path):
    l = open(path, "r").read().strip()

    S = []
    for i, c in enumerate(l):
        S.append(c)
        if len(S) >= 14:                
            if len(Counter("".join(S))) == len("".join(S)):
                return i + 1
            S.pop(0)


if __name__ == "__main__":

    print(p1(SAMPLE_INPUT_PATH))
    print(p1(INPUT_PATH))

    print(p2(SAMPLE_INPUT_PATH))
    print(p2(INPUT_PATH))