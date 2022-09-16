from forex_python.converter import CurrencyRates


def main():
    # The code below is for converting the amount in USD to PHP.
    rate = CurrencyRates()

    amount = float(input("Enter amount in USD: "))

    print(round(rate.convert('USD', 'PHP', amount), 2))


if __name__ == '__main__':
    main()
