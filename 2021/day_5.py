import os

ROOT_DIR = os.path.dirname(os.path.abspath(__file__)) 
SAMPLE_INPUT_PATH = ROOT_DIR + '\day_5_input_sample.txt'
INPUT_PATH = ROOT_DIR + "\day_5_input.txt"


def func(lines):
    lines_subset = [line for line in lines if line[0][0] == line[1][0] or line[0][1] == line[1][1]]
    plot = plot_line(lines_subset)
    return score_plot(plot)
    

def func2(lines):
    plot = plot_line2(lines)
    return score_plot(plot)   

def score_plot(plot):
    cnt_twos = 0
    for row in plot:
        for cell in row:
            if cell > 1:
                cnt_twos += 1

    return cnt_twos

def create_canvas(lines):
    x1 = 0
    y1 = 0
    for line in lines:
        if x1 < line[0][0] :
            x1 = line[0][0]

        if x1 < line[1][0]:
            x1 = line[1][0]

        if y1 < line[0][1]:
            y1 = line[0][1]

        if  y1 < line[1][1]:
            y1 = line[1][1]

    return [ [0]*(x1+1) for _ in range(y1+1) ]

def plot_line(lines):
    plot = create_canvas(lines)
    for line in lines:
        # vertical line (x1 = x2)
        if line[0][0] == line[1][0]:
            if line[0][1] < line[1][1]:
                for y in range(line[0][1], line[1][1]+1):
                    plot[y][line[0][0]] += 1
            else:
                for y in range(line[1][1], line[0][1]+1):
                    plot[y][line[0][0]] += 1

        # vertical line (y1 = y2)
        if line[0][1] == line[1][1]:
            if line[0][0] < line[1][0]:
                for x in range(line[0][0], line[1][0]+1):
                    plot[line[0][1]][x] += 1
            else: 
                for x in range(line[1][0], line[0][0]+1):
                    plot[line[0][1]][x] += 1

    return plot

def plot_line2(lines):
    plot = create_canvas(lines)       

    for line in lines:
        # vertical line (x1 = x2)
        if line[0][0] == line[1][0]:
            if line[0][1] < line[1][1]:
                for y in range(line[0][1], line[1][1]+1):
                    plot[y][line[0][0]] += 1
            else:
                for y in range(line[1][1], line[0][1]+1):
                    plot[y][line[0][0]] += 1

        # horizontal line (y1 = y2)
        elif line[0][1] == line[1][1]:
            if line[0][0] < line[1][0]:
                for x in range(line[0][0], line[1][0]+1):
                    plot[line[0][1]][x] += 1
            else: 
                for x in range(line[1][0], line[0][0]+1):
                    plot[line[0][1]][x] += 1
        # diagonal line
        else:
            points = coords_to_points(line)
            for point in points:
                plot[point[0]][point[1]] += 1
 
    return plot
            
def coords_to_points(line):
    m = (line[1][1] - line[0][1]) / (line[1][0] - line[0][0])
    c = line[0][1] - m * line[0][0]

    return [[int(m*x + c),x] for x in range(min(line[0][0], line[1][0]), max(line[0][0], line[1][0])+1)]

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
    print("Part 1 expected answer: {}, calculated answer: {}".format(5, func(lines)))
    print("Part 2 expected answer: {}, calculated answer: {}".format(12, func2(lines)))

    lines = process_input(INPUT_PATH)

    print("Challange data")
    print("Part 1 expected answer: {}, calculated answer: {}".format(6005, func(lines)))
    print("Part 2 expected answer: {}, calculated answer: {}".format(">23178; >23838", func2(lines)))

    