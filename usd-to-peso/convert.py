from forex_python.converter import CurrencyRates


def main():
    # The code below is for converting the amount in USD to PHP.
    rate = CurrencyRates()

    amount = float(input("Enter amount in USD: "))

    differential = rate.convert('USD', 'PHP', amount)

    print(f'₱ {differential:,.2f}')


if __name__ == '__main__':
    main()
