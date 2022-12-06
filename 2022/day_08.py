import os

ROOT_DIR = os.path.dirname(os.path.abspath(__file__)) 
SAMPLE_INPUT_PATH = ROOT_DIR + '/day_08_input_sample.txt'
INPUT_PATH = ROOT_DIR + "/day_08_input.txt"

def p1(path):
    return 0

def p2(path):
    return 0


if __name__ == "__main__":

    print(p1(SAMPLE_INPUT_PATH))
    print(p1(INPUT_PATH))

    print(p2(SAMPLE_INPUT_PATH))
    print(p2(INPUT_PATH))