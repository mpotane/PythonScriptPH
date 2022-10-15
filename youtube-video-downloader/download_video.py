from pytube import YouTube


"""
`yt = Youtube('https://www.youtube.com/watch?v=dQw4w9WgXcQ')`

This line of code creates a variable called `yt` and assigns it the value of the `Youtube` class.
The `Youtube` class is a class that is defined in the `pytube` library. The `Youtube` class takes in
a single argument, which is the URL of the YouTube video that you want to download. 

`yt.streams.get_by_itag(18).download()`

This line of code calls the `download` method on the `yt` variable. The `download` method is a
method that is defined in the `Stream` class, which is a class that is defined in the `pytube`
library. The `download` method takes in no arguments. 

The `yt` variable is an instance of
"""
def main():
    yt = YouTube('https://www.youtube.com/watch?v=dQw4w9WgXcQ')
    yt.streams.get_by_itag(18).download()


if __name__ == '__main__':
    main()
