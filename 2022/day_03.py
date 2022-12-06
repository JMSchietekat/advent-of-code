import os

ROOT_DIR = os.path.dirname(os.path.abspath(__file__)) 
SAMPLE_INPUT_PATH = ROOT_DIR + '/day_03_input_sample.txt'
INPUT_PATH = ROOT_DIR + "/day_03_input.txt"

I = "_abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

def p1(path):
    ans = 0
    
    with open(path) as file:
        for line in file:
            m = len(line) // 2
            a, b = line[:m], line[m:]
            c = set(a) & set(b)
            ans += I.index(next(iter(c)))

    return ans

def p2(path):
    ans = 0

    with open(path) as f:
        il = iter(f.read().split())

        while True:
            try:
                a, b, c = next(il), next(il), next(il)
            except StopIteration:
                return ans

            d = set(a) & set(b) & set(c)
            ans += I.index(next(iter(d)))
    
if __name__ == "__main__":

    print(p1(SAMPLE_INPUT_PATH))
    print(p1(INPUT_PATH))

    print(p2(SAMPLE_INPUT_PATH))
    print(p2(INPUT_PATH))

    