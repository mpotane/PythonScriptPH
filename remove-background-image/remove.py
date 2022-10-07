from rembg import remove
from PIL import Image


def main():
    """
    It takes an image and returns a new image with the background removed
    """
    img = Image.open('owl.jpg')
    out = remove(img)
    out.save('owl.png')


if __name__ == '__main__':
    # For more info visit https://github.com/danielgatis/rembg
    # you need to download the model first https://github.com/danielgatis/rembg#models
    main()
