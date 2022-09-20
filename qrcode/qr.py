import qrcode


def main():
    # You can put website link here <-.
    img = qrcode.make('https://cdn.vox-cdn.com/thumbor/WR9hE8wvdM4hfHysXitls9_bCZI=/0x0:1192x795/1400x1400/filters:focal(596x398:597x399)/cdn.vox-cdn.com/uploads/chorus_asset/file/22312759/rickroll_4k.jpg')
    img.save("qr.png")


if __name__ == '__main__':
    main()
