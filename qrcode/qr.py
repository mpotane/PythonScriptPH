import qrcode

img = qrcode.make('This is a QR code!') #You can put website link here <-.
img.save("qr.png")