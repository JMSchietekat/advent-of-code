import re, os
from collections import deque

ROOT_DIR = os.path.dirname(os.path.abspath(__file__)) 
SAMPLE_INPUT_PATH = ROOT_DIR + '/day_05_input_sample.txt'
INPUT_PATH = ROOT_DIR + "/day_05_input.txt"

def p1(path):
    with open(path) as f:
        C, M = f.read().split("\n\n")
        S = []

        for r in C.splitlines():
            for i, idx in enumerate(range(1, len(r), 4)):
                while i >= len(S):
                    S.append(deque())
                if r[idx] != " ":
                    S[i].append(r[idx])

        for m in M.splitlines():
            cnt, src, des = map(int, re.findall(r"\d+", m))
            for i in range(cnt):
                S[des - 1].appendleft(S[src - 1].popleft())

        return "".join(s[0] for s in S)

def p2(path):
    with open(path) as f:
        C, M = f.read().split("\n\n")
        S = []

        for r in C.splitlines():
            for i, idx in enumerate(range(1, len(r), 4)):
                while i >= len(S):
                    S.append(deque())
                if r[idx] != " ":
                    S[i].append(r[idx])

        for m in M.splitlines():
            cnt, src, des = map(int, re.findall(r"\d+", m))
            t = deque()
            for i in range(cnt):
                t.appendleft(S[src - 1].popleft())
            S[des - 1].extendleft(t)

        return "".join(s[0] for s in S)

if __name__ == "__main__":

    print(p1(SAMPLE_INPUT_PATH))
    print(p1(INPUT_PATH))

    print(p2(SAMPLE_INPUT_PATH))
    print(p2(INPUT_PATH))

   