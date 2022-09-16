from gtts import gTTS
# if you use GNU/Linux you might have to install pygobject for playsound to work.
from playsound import playsound


def main():
    # Tagalog = 'tl' btw
    sp = gTTS(text='Kumusta yung mundo mo', lang='tl', slow=False)
    sp.save('tunog.mp3')
    playsound('tunog.mp3')


if __name__ == '__main__':
    main()
