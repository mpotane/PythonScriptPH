import pandas as pd

# Reading the csv file and converting it to a json file.


def main():
    df = pd.read_csv('sample.csv')
    df.to_json('sample.json')


if __name__ == '__main__':
    main()
