import os

ROOT_DIR = os.path.dirname(os.path.abspath(__file__)) 
SAMPLE_INPUT_PATH = ROOT_DIR + '/day_01_input_sample.txt'
INPUT_PATH = ROOT_DIR + "/day_01_input.txt"

def p1(path):
    A = []
    s = 0

    with open(path) as f:
        for l in f:
            if l != '\n':
                s += int(l)
            else:
                A.append(s)
                s = 0

    A.sort(reverse=True)

    return A[0]

def p2(path):
    A = []
    s = 0

    with open(path) as f:
        for l in f:
            if l != '\n':
                s += int(l)
            else:
                A.append(s)
                s = 0

    A.sort(reverse=True)

    return A[0] + A[1] + A[2]

if __name__ == "__main__":

    print(p1(SAMPLE_INPUT_PATH))
    print(p1(INPUT_PATH))

    print(p2(SAMPLE_INPUT_PATH))
    print(p2(INPUT_PATH))

    