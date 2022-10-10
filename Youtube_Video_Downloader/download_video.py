from pytube import YouTube


def main():
    yt = Youtube('https://www.youtube.com/watch?v=dQw4w9WgXcQ')
    yt.streams.get_by_itag(18).download()


if __name__ == '__main__':
    main()
