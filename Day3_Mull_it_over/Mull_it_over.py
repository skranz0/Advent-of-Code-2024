import re


def main():
    memory = read_input("input.txt")
    pattern = re.compile("mul\(\d+,\d+\)|do\(\)|don\'t\(\)")

    result = 0
    skip = False
    for line in memory:
        matches = re.findall(pattern, line)
        for match in matches:
            if match == "don't()":
                skip = True
            elif match == "do()":
                skip = False
            else:
                if skip:
                    pass
                else:
                    result += eval(match)
    print(result)

def read_input(file):
    with open(file, "r") as f:
        lines = f.readlines()
    return lines

def mul(x: int, y: int) -> int:
    return x * y

if __name__ == '__main__':
    main()