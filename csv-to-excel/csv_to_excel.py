import pandas as pd


def main():
    df = pd.read_csv('test.csv')
    df.to_excel('test.xlsx')


if __name__ == '__main__':
    main()
