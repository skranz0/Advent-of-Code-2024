import pandas as pd
from tqdm import tqdm


def main():
    left_list, right_list = read_input("input.txt")

    first_star_solution = solve_first_star(left_list, right_list)
    print(f"The total distance is {first_star_solution}")

    second_star_solution = solve_second_star(left_list, right_list)
    print(f"The total similarity is {second_star_solution}")


def read_input(filename):
    df = pd.read_table(filename, sep='  ', header=None)
    left_list = df[0].tolist()
    right_list = df[1].tolist()
    return left_list, right_list

def solve_first_star(left_list, right_list):
    left_list_sorted = sorted(left_list)
    right_list_sorted = sorted(right_list)

    total_distance = 0
    while len(left_list_sorted) != 0 and len(right_list_sorted) != 0:
        distance = abs(left_list_sorted.pop() - right_list_sorted.pop())
        total_distance += distance

    return total_distance

def solve_second_star(left_list, right_list):
    total_similarity = 0
    for i in tqdm(left_list):
        count_in_right = 0
        for j in right_list:
            if i == j:
                count_in_right += 1
        similarity = i * count_in_right
        total_similarity += similarity

    return total_similarity


if __name__ == '__main__':
    main()