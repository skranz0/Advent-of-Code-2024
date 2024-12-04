import numpy as np


def main():
    word_search = read_input("input.txt")
    horizontal = search_horizontal(word_search)
    vertical = search_vertical(word_search)
    diagonal = search_diagonal(word_search)
    print(f"{horizontal} + {vertical} + {diagonal} = {horizontal + vertical + diagonal}")

def read_input(filename):
    with open(filename, 'r') as f:
        input = f.readlines()
        output = []
        for line in input:
            output.append(list(line)[0:-1])
    return output

def search_horizontal(word_search):
    count = 0
    for line in word_search:
        if len(line) >= 4:
            for i in range(len(line)):
                print(line[i:i+4])
                if line[i:i+4] == ['X','M','A','S'] or line[i:i+4] == ['S','A','M','X']:
                    count += 1
    return count
def search_vertical(word_search):
    word_matrix = np.asmatrix(word_search).transpose().tolist()
    count = search_horizontal(word_matrix)
    return count

def search_diagonal(word_search):
    word_matrix = np.asmatrix(word_search)
    word_matrix_t = np.fliplr(word_matrix).transpose()
    diagonals, diagonals_t = [[],[]]
    for i in range(-len(word_matrix), len(word_matrix)):
        diagonals.append(np.diag(word_matrix, i).tolist())
        diagonals_t.append(np.diag(word_matrix_t, i).tolist())
    count = search_horizontal(diagonals) + search_horizontal(diagonals_t)
    return count

if __name__ == '__main__':
    main()