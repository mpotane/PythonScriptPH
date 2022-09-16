import shutil


def main():
    # Copy File (source, newfile)
    shutil.copyfile('text2copy.txt', 'text-copied.txt')


if __name__ == '__main__':
    main()
