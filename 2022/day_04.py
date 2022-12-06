import os

ROOT_DIR = os.path.dirname(os.path.abspath(__file__)) 
SAMPLE_INPUT_PATH = ROOT_DIR + '/day_04_input_sample.txt'
INPUT_PATH = ROOT_DIR + "/day_04_input.txt"

def text_to_set(t):
    s, e = t.split("-")
    return set(range(int(s), int(e) + 1))

def p1(path):
    ans = 0
    with open(path) as f:
        for l in f:
            a, b = l.strip().split(",")
            a = set(text_to_set(a))
            b = set(text_to_set(b))
            if len(a - b) == 0 or len(b - a) == 0:
                ans += 1
    return ans


def p2(path):
    ans = 0
    with open(path) as f:
        for l in f:
            a, b = l.strip().split(",")
            a = set(text_to_set(a))
            b = set(text_to_set(b))
            if len(a & b) > 0:
                ans += 1
    return ans
    

if __name__ == "__main__":

    print(p1(SAMPLE_INPUT_PATH))
    print(p1(INPUT_PATH))

    print(p2(SAMPLE_INPUT_PATH))
    print(p2(INPUT_PATH))

    