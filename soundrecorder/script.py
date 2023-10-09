import sounddevice
from scipy.io.wavfile import write


def main():
    fs = 44100  # Sample rate
    seconds = 10  # Duration of recording

    myrecording = sounddevice.rec(int(seconds * fs), samplerate=fs, channels=2)
    sounddevice.wait()  # Wait until recording is finished
    write("output.wav", fs, myrecording)  # Save as WAV file

if __name__ == "__main__":
    main()