import os

ROOT_DIR = os.path.dirname(os.path.abspath(__file__)) 
SAMPLE_INPUT_PATH = ROOT_DIR + '\day_3_input_sample.txt'
INPUT_PATH = ROOT_DIR + "\day_3_input.txt"

def life_support_rating(arr):
    o2_generator_rating = int(arr2str(rec_search(arr, 0, 1)),2)
    co2_scrubber_rating = int(arr2str(rec_search(arr, 0, 0)),2)

    return o2_generator_rating * co2_scrubber_rating

def rec_search(arr, pos, keep):
    temp = []
    target = []

    if len(arr) > 1:
        target = calc_gamma(arr) if keep == 1 else calc_epsilon_from_gamma(calc_gamma(arr))

    # for i in range(len(arr)):
    #     if i == pos:
    #         temp.append(1)
    #     else:
    #         temp.append(0)

    # if arr2str(temp) == arr2str(target):
    #     return temp    
 
    for i in arr:
        if len(arr) == 2:
            if int(i[pos]) == keep:
                temp.append(i)
        elif int(i[pos]) == target[pos]:
            temp.append(i)

    if len(temp) == 2:
        return temp[0] if temp[0][pos] == keep else temp[1]
    if len(temp) == 1:
        return temp[0]
    else:
        return rec_search(temp, pos + 1, keep)

def power_consumption(arr):
    gammaArr = calc_gamma(arr)
    epsilonArr = calc_epsilon_from_gamma(gammaArr)

    gamma = int(arr2str(gammaArr),2)
    epsilon = int(arr2str(epsilonArr),2)

    return gamma * epsilon

def calc_gamma(arr):
    
    gamma = [0] * len(arr[0])
    threshold = len(arr) / 2

    for i in arr:
        for x, j in enumerate(i):
            if j == '1': gamma[x] += 1

    gamma2 = []
    # [0] * len(arr[0])

    for i in gamma:
        if i > threshold: gamma2.append(1)
        else: gamma2.append(0)

    return gamma2

def calc_epsilon_from_gamma(gamma):
    return inverse(gamma)    

def inverse(arr):
    temp_arr = []
    for i in arr:
        if i == 0: temp_arr.append(1)
        else: temp_arr.append(0)

    return temp_arr

def arr2str(arr):
    temp = ""
    for i in arr:
        temp += str(i)

    return temp

def power_consumption2(arr):
    bits = len(arr[0])

    A = [[0 for _ in range(bits)] for _ in range(2)]

    for i in arr:
        

    gamma = ''
    epsilon = ''

    



if __name__ == "__main__":
    
    arr = [line.replace("\n","") for line in open(SAMPLE_INPUT_PATH, "r")]

    print("Sample data")
    print("Part 1 expected answer: {}, calculated answer: {}".format(198, power_consumption2(arr)))
    print("Part 2 expected answer: {}, calculated answer: {}".format(230, life_support_rating(arr)))

    arr = [line.replace("\n","") for line in open(INPUT_PATH, "r")]

    print("Challange data")
    print("Part 1 expected answer: {}, calculated answer: {}".format(3969000, power_consumption2(arr)))
    print("Part 2 expected answer: {}, calculated answer: {}".format(4267809, life_support_rating(arr)))

    