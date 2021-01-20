#download tesseract.exe -> https://github.com/UB-Mannheim/tesseract/wiki
#pip install pytesseract

import os
import pyautogui
from PIL import Image
from pytesseract import *

#included tesseract.exe from downloaded directory & path to save txt file
pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
saving_path = 'C:/Users/hp/Desktop/imagetotexts/'

#taking input of image path & filename for saving txt
#example: C:/Users/hp/Desktop/myimage.png
imgpath = input("Image Path: ")
fname = input("File Name: ")

#generating text from image
img=Image.open(imgpath)
text=pytesseract.image_to_string(img)
#geting directory path to save .txt file -> create -> write -> close
actualname = os.path.join(saving_path, fname+".txt")
file=open(actualname, "w")
file.write(text)
file.close()

#showing the txt file in terminal/command prompt
os.system("cat "+actualname)