import PIL
from PIL import Image
from tkinter.filedialog import *


fl=askopenfilenames()
img = Image.open(fl[0])
img.save("output.jpg", "JPEG", optimize = True, quality = 10)