import os

ROOT_DIR = os.path.dirname(os.path.abspath(__file__)) 
SAMPLE_INPUT_PATH = ROOT_DIR + '/day_01_input_sample.txt'
INPUT_PATH = ROOT_DIR + "/day_01_input.txt"

def p1(input_path):
    A = []
    cnt = 1

    with open(input_path) as file:
        for line in file:
            if line == '\n':
                cnt += 1
            else:
                t = int(line.replace('\n',''))
                if cnt > len(A):
                     A.append(t)
                else:
                    A[cnt-1] += t

    A.sort(reverse=True)

    return A[0]

def p2(input_path):
    A = []
    cnt = 1

    with open(input_path) as file:
        for line in file:
            if line == '\n':
                cnt += 1
            else:
                t = int(line.replace('\n',''))
                if cnt > len(A):
                     A.append(t)
                else:
                    A[cnt-1] += t

    A.sort(reverse=True)

    return A[0] + A[1] + A[2]

if __name__ == "__main__":

    print(p1(SAMPLE_INPUT_PATH))
    print(p1(INPUT_PATH))

    print(p2(SAMPLE_INPUT_PATH))
    print(p2(INPUT_PATH))

    