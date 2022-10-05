import pandas as pd


def main():
    df = pd.read_csv('text.csv')
    df.to_excel('text.xlsx')

if __name__ == '__main__':
    main()
