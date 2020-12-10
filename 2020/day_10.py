inputFilePath = "C:/git-jmschietekat/advent-of-code/2020/day_10_input.txt"

if __name__ == "__main__":
    arr = [int(line.replace('\n', '')) for line in open(inputFilePath, "r")]
    arr.append(0)
    arr.sort()

    delta1 = 0
    delta3 = 1  # Built-in adapter is always 3 higher

    for i, e in enumerate(arr):
        if i == 0:
            continue

        if e - arr[i-1] > 3:
            print('Too large difference')

        if e - arr[i-1] == 3:
            delta3 += 1

        if e - arr[i-1] == 1:
            delta1 += 1

    print("Part 1: {} x 1-jolt differences multiplied by {} x 3-jolt differences = {}.".format(delta1, delta3, delta1 * delta3))