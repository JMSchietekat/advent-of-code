import os

ROOT_DIR = os.path.dirname(os.path.abspath(__file__)) 
SAMPLE_INPUT_PATH = ROOT_DIR + '\day_1_input_sample.txt'
INPUT_PATH = ROOT_DIR + "\day_1_input.txt"

def count_pos_grad_windowed_3(arr):
    cnt = 0
    prev_sum = 0
    total = 0

    for i, depth in enumerate(arr):
        if i > 1:
            total = depth + arr[i-1] + arr[i-2]
            if prev_sum == 0:
                prev_sum = total
                continue
            else :
                delta = total - prev_sum
                if delta > 0:
                    cnt += 1

        prev_sum = total

    return cnt

def count_positive_gradients(arr):
    cnt = 0

    for i, depth in enumerate(arr):
        if i > 0:
            delta = depth - arr[i-1]
            if delta > 0:
                cnt += 1

    return cnt


if __name__ == "__main__":
    arr = [int(line.replace('\n', '')) for line in open(SAMPLE_INPUT_PATH, "r")]

    print("Sample data")
    print("Part 1 expected answer: {}, calculated answer: {}".format(7, count_positive_gradients(arr)))
    print("Part 2 expected answer: {}, calculated answer: {}".format(5, count_pos_grad_windowed_3(arr)))

    arr = [int(line.replace('\n', '')) for line in open(INPUT_PATH, "r")]

    print("Challange data")
    print("Part 1 expected answer: {}, calculated answer: {}".format(1709, count_positive_gradients(arr)))
    print("Part 2 expected answer: {}, calculated answer: {}".format(1761, count_pos_grad_windowed_3(arr)))