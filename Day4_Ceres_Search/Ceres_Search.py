import numpy as np


def main():
    word_search = read_input("test.txt")
    #print(word_search)
    horizontal = search_horizontal(word_search)
    vertical = search_vertical(word_search)

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
        for i in range(len(line)-3):
            if line[i:i+4] == ['X','M','A','S'] or line[i:i+4] == ['S','A','M','X']:
                count += 1
    return count
def search_vertical(word_search):
    word_matrix = np.asmatrix(word_search).transpose().tolist()
    count = search_horizontal(word_matrix)
    return count



if __name__ == '__main__':
    main()