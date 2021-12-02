sample_input_file_path = "C:/git-jmschietekat/advent-of-code/2021/day_1_input_sample.txt"
input_file_path = "C:/git-jmschietekat/advent-of-code/2021/day_1_input.txt"

def count_positive_gradients(arr, window_size = 1):
    cnt = 0
    prev_total = 0
    total = 0

    ints()
    
    zip()
    for i, _ in enumerate(arr):
        if i > 0:
            total = window_sum(arr, window_size, i)
        
        if i > window_size:
            delta = total - prev_total
            if delta > 0:
                cnt += 1

        prev_total = total

    return cnt

def window_sum(arr, window_size, start_index):
    assert window_size > 0, "Window size must be at least 1"
    assert window_size <= len(arr), "The maximium window size must be smaller or equal to the array lenght."

    if window_size > 1:
        return arr[start_index - window_size - 1] + window_sum(arr, window_size - 2, start_index)
    if window_size == 1:
        return arr[start_index]
    else:
        return 0

if __name__ == "__main__":
    arr = [int(line.replace('\n', '')) for line in open(sample_input_file_path, "r")]

    print("Sample data")
    print("Part 1 expected answer: {}, calculated answer: {}".format(7, count_positive_gradients(arr)))
    print("Part 2 expected answer: {}, calculated answer: {}".format(5, count_positive_gradients(arr, 3)))

    arr = [int(line.replace('\n', '')) for line in open(input_file_path, "r")]

    print("Challange data")
    print("Part 1 expected answer: {}, calculated answer: {}".format(1709, count_positive_gradients(arr)))
    print("Part 2 expected answer: {}, calculated answer: {}".format(1761, count_positive_gradients(arr, 3)))

    print(window_sum([1, 2, 3, 4], 1, 3))
    print(window_sum([1, 2, 3, 4], 1, 3))
    print(window_sum([1, 2, 3, 4], 2, 3))