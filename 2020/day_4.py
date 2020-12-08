import re

inputFilePath = "C:/git-jmschietekat/advent-of-code/2020/day_4_input.txt"


def fileToArr(filePath):
    fileObject = open(filePath, "r")

    arr = []

    tempLine = ''

    for line in fileObject:
        tempLine += line.replace('\n', ' ')

        if line == '\n':
            arr.append(tempLine)
            tempLine = ''

    arr.append(tempLine)

    return arr


def isValidPassportPart1(line):
    regex = re.search(
        r"(?=.*\bbyr\b)(?=.*\biyr\b)(?=.*\beyr\b)(?=.*\bhgt\b)(?=.*\bhcl\b)(?=.*\becl\b)(?=.*\bpid\b).*", line)

    if regex:
        return True
    else:
        return False


def isValidPassportPart2(line):
    pattern = r'(?=.*\bbyr:(?P<byr>[0-9]{4}\d*)\b)'
    pattern += r'(?=.*\biyr:(?P<iyr>[0-9]{4}\d*)\b)'
    pattern += r'(?=.*\beyr:(?P<eyr>[0-9]{4}\d*)\b)'
    pattern += r'(?=.*\bhgt:(?P<hgt>\d{2,3})(?P<hgtunit>(cm|in))\b)'
    pattern += r'(?=.*\bhcl:#([0-9]|[a-f]){6}\b)'
    pattern += r'(?=.*\becl:(amb|blu|brn|gry|grn|hzl|oth)\b)'
    pattern += r'(?=.*\bpid:[0-9]{9}\b).*'

    regex = re.search(pattern, line)

    if not regex:
        return False

    if int(regex.group('byr')) < 1920 or int(regex.group('byr')) > 2002:
        return False

    if int(regex.group('iyr')) < 2010 or int(regex.group('iyr')) > 2020:
        return False

    if int(regex.group('eyr')) < 2020 or int(regex.group('eyr')) > 2030:
        return False

    if 'cm' in regex.group('hgtunit'):
        if int(regex.group('hgt')) < 150 or int(regex.group('hgt')) > 193:
            return False

    if 'in' in regex.group('hgtunit'):
        if int(regex.group('hgt')) < 59 or int(regex.group('hgt')) > 76:
            return False

    return True


if __name__ == "__main__":
    arr = fileToArr(inputFilePath)

    validPassports = 0

    for passport in arr:
        if isValidPassportPart1(passport):
            validPassports += 1

    print("Part 1: {} valid passports were found, not checking for 'cid'".format(
        validPassports))

    validPassports = 0

    for passport in arr:
        if isValidPassportPart2(passport):
            validPassports += 1

    print("Part 2: {} valid passports were found.".format(
        validPassports))
