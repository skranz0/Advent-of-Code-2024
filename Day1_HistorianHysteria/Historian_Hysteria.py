import pandas as pd


def main():
    left_list, right_list = read_input("input.txt")

    first_star_solution = solve_first_star(left_list, right_list)
    print(f"The total distance is {first_star_solution}")


def read_input(filename):
    df = pd.read_table(filename, sep='  ', header=None)
    left_list = df[0].tolist()
    right_list = df[1].tolist()
    return left_list, right_list

def solve_first_star(left_list, right_list):
    left_list.sort()
    right_list.sort()

    total_distance = 0
    while len(left_list) != 0 and len(right_list) != 0:
        distance = abs(left_list.pop() - right_list.pop())
        total_distance += distance

    return total_distance

def solve_second_star(left_list, right_list):
    pass

if __name__ == '__main__':
    main()