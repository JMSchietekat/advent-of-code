import os

ROOT_DIR = os.path.dirname(os.path.abspath(__file__)) 
SAMPLE_INPUT_PATH = ROOT_DIR + '/day_02_input_sample.txt'
INPUT_PATH = ROOT_DIR + "/day_02_input.txt"

def score1(a,b):
    # opponent: A rock B paper C scissors
    # you: X Rock Y paper Z scissors
    # score rock 1 2 paper 3 scissors
    # 0 lost 3 draw 6 win
    if a == "A": #rock
        if b == "X": #rock
            return 3 + 1
        if b == "Y": #paper
            return 6 + 2
        if b == "Z": #scissors
            return 0 + 3

    if a == "B": #paper
        if b == "X": #rock
            return 0 + 1
        if b == "Y": #paper
            return 3 + 2
        if b == "Z": #scissors
            return 6 + 3

    if a == "C": #scissors
        if b == "X": #rock
            return 6 + 1
        if b == "Y": #paper
            return 0 + 2
        if b == "Z": #scissors
            return 3 + 3

def score2(a,b):
    # x lose y draw z win
    c = ''
    if b == "Y":
        c = "D"
    elif b == "X":
        c = "L"
    elif b == 'Z':
        c = "W"

    # opponent: A rock B paper C scissors
    # you: X Rock Y paper Z scissors
    # score rock 1 2 paper 3 scissors
    # 0 lost 3 draw 6 win
    if a == "A": #rock
        if c == "W":
            b = "Y"
        elif c == "D":
            b = "X"
        elif c == "L":
            b = "Z"

        if b == "X": #rock
            return 3 + 1
        if b == "Y": #paper
            return 6 + 2
        if b == "Z": #scissors
            return 0 + 3

    if a == "B": #paper
        if c == "W":
            b = "Z"
        elif c == "Y":
            b = "X"
        elif c == "L":
            b = "X"

        if b == "X": #rock
            return 0 + 1
        if b == "Y": #paper
            return 3 + 2
        if b == "Z": #scissors
            return 6 + 3

    if a == "C": #scissors
        if c == "W":
            b = "X"
        elif c == "D":
            b = "Z"
        elif c == "L":
            b = "Y"

        if b == "X": #rock
            return 6 + 1
        if b == "Y": #paper
            return 0 + 2
        if b == "Z": #scissors
            return 3 + 3

    

def p1(path):
    A = []
    t = 0

    with open(path) as f:
        for l in f:
            A.append(l.replace('\n','').split(' '))

    for k in A:
        t += score1(k[0],k[1])

    return t

def p2(path):
    A = []
    t = 0

    with open(path) as f:
        for l in f:
            A.append(l.replace('\n','').split(' '))

    for k in A:
        t += score2(k[0],k[1])

    return t
    

if __name__ == "__main__":

    print(p1(SAMPLE_INPUT_PATH))
    print(p1(INPUT_PATH))

    print(p2(SAMPLE_INPUT_PATH))
    print(p2(INPUT_PATH))

    