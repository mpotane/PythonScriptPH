from forex_python.bitcoin import BtcConverter


def main():
    btc = BtcConverter()  # force_decimal=True to get Decimal rates
    price = btc.get_latest_price('PHP')

    print(f'₱ {price:,.2f}')


if __name__ == '__main__':
    main()
