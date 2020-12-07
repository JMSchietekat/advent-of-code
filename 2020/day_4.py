import re

inputFilePath = "C:/git-jmschietekat/advent-of-code/2020/day_4_input.txt"


def fileToArr(filePath):
    fileObject = open(filePath, "r")

    arr = []

    tempLine = ''

    for i, line in enumerate(fileObject):
        tempLine += line.replace('\n',' ')

        if line == '\n':
            arr.append(tempLine)
            tempLine = ''
        
    arr.append(tempLine)

    return arr

def isValidPassport(line):
    regex = re.search(r"(?=.*\bbyr\b)(?=.*\biyr\b)(?=.*\beyr\b)(?=.*\bhgt\b)(?=.*\bhcl\b)(?=.*\becl\b)(?=.*\bpid\b).*", line)
    print(line, regex)
    if regex: 
        return True
    else:
        return False

if __name__ == "__main__":
    arr = fileToArr(inputFilePath)

    validPassports = 0

    for passport in arr:
        if isValidPassport(passport):
            validPassports += 1

    print("Part 1: {} valid password were found, not checking for 'cid'".format(validPassports))

    
