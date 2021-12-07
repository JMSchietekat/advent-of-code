import os

ROOT_DIR = os.path.dirname(os.path.abspath(__file__)) 
SAMPLE_INPUT_PATH = ROOT_DIR + '\day_04_input_sample.txt'
INPUT_PATH = ROOT_DIR + "\day_04_input.txt"

def func2(number, boards):
    total_boards = len(boards)
    win_cnt = 0
    for n in number:
        for i, board in enumerate(boards):
            boards[i] = update_board(board, n)
            if not boards[i] == []:
                win, winning_board = check_win(boards[i])
                if win == True:
                    boards[i]= []
                    win_cnt += 1
                    if win_cnt == total_boards:
                        return check_sum(winning_board, n)

def func(numbers, boards):
    for n in numbers:
        for i, board in enumerate(boards):
            boards[i] = update_board(board, n)
            win, winning_board = check_win(boards[i])
            if win == True:
                return check_sum(winning_board, n)

def check_sum(board, n):
    total = 0
    for col in range(5):
        for row in range(5):
            if board[row][col][1] == 0: total += board[row][col][0]

    return total * n

def update_board(board, number):
    for row in board:
        for cell in row:
            if cell[0] == number:
                cell[1] = 1

    return board

def check_win(board):
    row_cnt = 0
    col_cnt = 0

    for col in range(5):
        row_cnt = 0
        col_cnt = 0
        for row in range(5):
            if board[row][col][1] == 1: col_cnt += 1
            if board[col][row][1] == 1: row_cnt += 1
            else: continue

        if col_cnt == 5 or row_cnt == 5:
            return True, board

    return False, board

def try_parse_int(string):
    try:
        int(string)
        return True
    except ValueError:
        return False

def process_input(input_path):
    numbers = []
    boards = []
    board = []
    with open(input_path) as file:
        for i, line in enumerate(file):
            if i == 0:
                numbers = [int(x) for x in line.split(",")]
            else:
                row = []
                if line == "\n":
                    if len(board) == 5:
                        boards.append(board)
                        board = []
                else:
                    row = [[int(x),0] for x in line.split(" ") if try_parse_int(x) == True]
                    board.append(row)

    boards.append(board)

    return numbers, boards
                


if __name__ == "__main__":

    print("Sample data")

    numbers, boards = process_input(SAMPLE_INPUT_PATH) 
    print("Part 1 expected answer: {}, calculated answer: {}".format(4512, func(numbers, boards)))

    numbers, boards = process_input(SAMPLE_INPUT_PATH)
    print("Part 2 expected answer: {}, calculated answer: {}".format(1924, func2(numbers, boards)))

    print("Challange data")

    numbers, boards = process_input(INPUT_PATH)
    print("Part 1 expected answer: {}, calculated answer: {}".format(8442, func(numbers, boards)))

    numbers, boards = process_input(INPUT_PATH)
    print("Part 2 expected answer: {}, calculated answer: {}".format(4590, func2(numbers, boards)))

    