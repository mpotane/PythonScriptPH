from PIL import Image
# It converts a JPEG image to a PDF file


def main():
    image_1 = Image.open('rickroll_4k.jpg')
    img_1 = image_1.convert('RGB')
    img_1.save('rickroll_4k.pdf')


if __name__ == '__main__':
    main()
