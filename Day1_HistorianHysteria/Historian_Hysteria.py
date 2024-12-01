import pandas as pd


def main():
    location_ids = read_input("input.txt")
    print(location_ids)

def read_input(filename):
    df = pd.read_table(filename, sep='  ', header=None)
    df.rename(columns={df.columns[0]: 'left_list', df.columns[1]: 'right_list'}, inplace=True)
    return df

if __name__ == '__main__':
    main()