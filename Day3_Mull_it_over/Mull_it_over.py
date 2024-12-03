import re


def main():
    memory = read_input("input.txt")

    result = 0
    for line in memory:
        matches = re.findall("mul\(\d+,\d+\)", line)
        for match in matches:
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