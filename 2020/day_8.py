inputFilePath = "C:/git-jmschietekat/advent-of-code/2020/day_8_input.txt"


def mapDay8(text):
    cmd, arg = (text).replace('\n', '').split(' ')

    if cmd == 'acc':
        cmd = acc
    if cmd == 'nop':
        cmd = nop
    if cmd == 'jmp':
        cmd = jmp

    return cmd, int(arg), 0


def nop(program, stack, accumulator):
    pc = stack[-1]

    if program[pc][2] == 1:
        failWith(program, stack, accumulator)
        return

    program[pc] = (program[pc][0], program[pc][1], 1)
    stack.append(pc + 1)

    if stack[-1] >= len(program):
        print("Terminated, accumulator: {}".format(accumulator))
        return

    program[stack[-1]][0](program, stack, accumulator)


def jmp(program, stack, accumulator):
    pc = stack[-1]

    if program[pc][2] == 1:
        failWith(program, stack, accumulator)
        return

    program[pc] = (program[pc][0], program[pc][1], 1)
    stack.append(pc + program[pc][1])

    if stack[-1] >= len(program):
        print("Terminated, accumulator: {}".format(accumulator))
        return

    program[stack[-1]][0](program, stack, accumulator)


def acc(program, stack, accumulator):
    pc = stack[-1]

    if program[pc][2] == 1:
        failWith(program, stack, accumulator)
        return

    program[pc] = (program[pc][0], program[pc][1], 1)
    accumulator += program[pc][1]
    stack.append(pc + 1)

    if stack[-1] >= len(program):
        print("Terminated, accumulator: {}".format(accumulator))
        return

    program[stack[-1]][0](program, stack, accumulator)


def failWith(program, stack, accumulator):
    print('Start of recursion, accumulator: {}'.format(accumulator))
    # for i, pc in enumerate(stack[::-1]):
    #     print('{}: {}'.format(i, intructionToString(program, pc)))
    #     if i > 10:
    #         break

def intructionToString(program, pc):
    return ("program counter: {}, command: {}, argument: {}".format(pc, program[pc][0].__name__, program[pc][1]))

def swopCommand(program, pos):
    copyProgram = program[:]

    if copyProgram[pos][0] == nop:
        copyProgram[pos] = (jmp, copyProgram[pos][1], 0)
        return copyProgram

    if copyProgram[pos][0] == jmp:
        copyProgram[pos] = (nop, copyProgram[pos][1], 0)
        return copyProgram

    return None

def run(program):
    if program:
        stack = [0]
        accumulator = 0
        program[stack[-1]][0](program, stack, accumulator)

if __name__ == "__main__":
    program = [mapDay8(line) for line in open(inputFilePath, "r")]
    
    print("Part 1")
    run(program)

    program = [mapDay8(line) for line in open(inputFilePath, "r")]

    print("Part 2")
    for itr in range(len(program)):
        run(swopCommand(program, itr))
