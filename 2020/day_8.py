inputFilePath = "C:/git-jmschietekat/advent-of-code/2020/day_8_input.txt"

def mapDay8(text):
    cmd, arg = (text).replace('\n','').split(' ')

    if cmd == 'acc':
        cmd = acc
    if cmd == 'nop':
        cmd = nop
    if cmd == 'jmp':
        cmd = jmp

    return cmd, int(arg), 0


def nop(instructions, programCounter, accumulator):
    instructions[programCounter] = (instructions[programCounter][0], instructions[programCounter][1], 1)
    programCounter += 1    
    
    if instructions[programCounter][2] == 1:
        print('Part 1: Start of infinte loop at program counter: {}, accumulator: {}, command: {}, argument: {}'.format(programCounter, accumulator, instructions[programCounter][0].__name__, instructions[programCounter][1]))
        return

    instructions[programCounter][0](instructions, programCounter, accumulator)


def jmp(instructions, programCounter, accumulator):
    instructions[programCounter] = (instructions[programCounter][0], instructions[programCounter][1], 1)
    programCounter += instructions[programCounter][1]
    
    if instructions[programCounter][2] == 1:
        print('Part 1: Start of infinte loop at program counter: {}, accumulator: {}, command: {}, argument: {}'.format(programCounter, accumulator, instructions[programCounter][0].__name__, instructions[programCounter][1]))
        return

    instructions[programCounter][0](instructions, programCounter, accumulator)

def acc(instructions, programCounter, accumulator):
    instructions[programCounter] = (instructions[programCounter][0], instructions[programCounter][1], 1)
    accumulator += instructions[programCounter][1]
    programCounter += 1    
    
    if instructions[programCounter][2] == 1:
        print('Part 1: Start of infinte loop at program counter: {}, accumulator: {}, command: {}, argument: {}'.format(programCounter, accumulator, instructions[programCounter][0].__name__, instructions[programCounter][1]))
        return

    instructions[programCounter][0](instructions, programCounter, accumulator)

if __name__ == "__main__":
    instructions = [mapDay8(line) for line in open(inputFilePath, "r")]
    programCounter = 0
    accumulator = 0

    instructions[programCounter][0](instructions, programCounter, accumulator)
    print('done')


    

    