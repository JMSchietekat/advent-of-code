import os

ROOT_DIR = os.path.dirname(os.path.abspath(__file__)) 
SAMPLE_INPUT_PATH = ROOT_DIR + '\day_07_input_sample.txt'
INPUT_PATH = ROOT_DIR + "\day_07_input.txt"

def calc1(arr):
    S = arr
    S.sort()
    median = S[len(S)//2]

    return cost1(S, median)

def cost1(arr, pos):
    total_fual = 0
    for a in arr:
        total_fual += abs(a - pos)

    return total_fual

def calc2(arr):
    S = arr
    max_score = 1e9
    for r in range(S[0], S[-1]):
        score = 0
        for v in S:
            score += cost3(abs(v-r))
        if score < max_score:
            max_score = score
        else: return int(max_score)
    
def cost2(moves):
    if moves == 0:
        return 0
    if moves == 1:
        return 1
    
    return moves + cost2(moves-1)

def cost3(moves):
    return moves*(moves+1)/2

if __name__ == "__main__":

    print("Sample data")

    arr = [int(v) for v in open(SAMPLE_INPUT_PATH, "r").read().strip().split(",")]
    print("Part 1 expected answer: {}, calculated answer: {}".format(37, calc1(arr)))
    print("Part 2 expected answer: {}, calculated answer: {}".format(168, calc2(arr)))

    print("Challange data")

    arr = [int(v) for v in open(INPUT_PATH, "r").read().strip().split(",")]
    print("Part 1 expected answer: {}, calculated answer: {}".format(343441, calc1(arr)))
    print("Part 2 expected answer: {}, calculated answer: {}".format(98925151, calc2(arr)))

    