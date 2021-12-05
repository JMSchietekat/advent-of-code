import os

ROOT_DIR = os.path.dirname(os.path.abspath(__file__)) 
SAMPLE_INPUT_PATH = ROOT_DIR + '\day_5_input_sample.txt'
INPUT_PATH = ROOT_DIR + "\day_5_input.txt"


def part1(lines):
    lines_subset = [line for line in lines if line[0][0] == line[1][0] or line[0][1] == line[1][1]]
    plot = plot_line(lines_subset)
    return score_plot(plot)
    

def part2(lines):
    plot = plot_line(lines)
    return score_plot(plot)   

def score_plot(plot):
    score = 0
    for row in plot:
        for cell in row:
            if cell > 1:
                score += 1

    return score

def init_plot(lines):
    x1 = 0
    y1 = 0
    for line in lines:
        x_max = max(line[0][0], line[1][0]) + 1
        if x1 < x_max:
            x1 = x_max

        y_max = max(line[0][1], line[1][1]) + 1 
        if y1 < y_max:
            y1 = y_max

    return [ [0]*(x1) for _ in range(y1) ]

def plot_line(lines):
    plot = init_plot(lines)       

    for line in lines:
        points = []
        
        # vertical line (x1 = x2)
        if line[0][0] == line[1][0]:
            points = [ [y, line[0][0]] for y in range(min(line[0][1], line[1][1]), max(line[0][1], line[1][1])+1) ]

        # horizontal line (y1 = y2)
        elif line[0][1] == line[1][1]:
            points = [ [line[0][1], x] for x in range(min(line[0][0], line[1][0]), max(line[0][0], line[1][0])+1) ]
        
        # diagonal line
        else:
            m = (line[1][1] - line[0][1]) / (line[1][0] - line[0][0])
            c = line[0][1] - m * line[0][0]
            points = [ [int(m*x + c),x] for x in range(min(line[0][0], line[1][0]), max(line[0][0], line[1][0])+1)]
        
        for point in points:
            plot[point[0]][point[1]] += 1
 
    return plot
            
def process_input(input_path):
    lines = []

    with open(input_path) as file:
        for line in file:
            coord1, coord2 = line.replace(" ","").replace("\n","").split('->')
            coord1 = [int(x) for x in coord1.split(",")]
            coord2 = [int(x) for x in coord2.split(",")]
            lines.append((coord1, coord2))
       
       
    return lines

if __name__ == "__main__":

    lines = process_input(SAMPLE_INPUT_PATH)

    print("Sample data")
    print("Part 1 expected answer: {}, calculated answer: {}".format(5, part1(lines)))
    print("Part 2 expected answer: {}, calculated answer: {}".format(12, part2(lines)))

    lines = process_input(INPUT_PATH)

    print("Challange data")
    print("Part 1 expected answer: {}, calculated answer: {}".format(6005, part1(lines)))
    print("Part 2 expected answer: {}, calculated answer: {}".format(23864, part2(lines)))

    