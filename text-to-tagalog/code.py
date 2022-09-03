from gtts import gTTS
from playsound import playsound #if you use GNU/Linux you might have to install pygobject for playsound to work.

sp=gTTS(text='Kumusta yung mundo mo',lang='tl',slow=False)
sp.save('tunog.mp3')
playsound('tunog.mp3')