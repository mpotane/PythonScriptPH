import qrcode


def main():
    # You can put website link here <-.
    img = qrcode.make('This is a QR code!')
    img.save("qr.png")


if __name__ == '__main__':
    main()
