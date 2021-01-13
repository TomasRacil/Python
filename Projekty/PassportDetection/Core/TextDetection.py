import cv2 #openCV
import os #pro mazání souboru
import pytesseract #OCR pip install tesseract; pip install pytesseract; nutno stáhnout balíček z webu
from PIL import Image #pip install pillow - pro načítání obrázků do tesseract
import Core.picturePreprocessor as pic

pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files/Tesseract-OCR/tesseract' #cesta k nainstalovanému tesseract

def recognize(picture):	
    cv2.imwrite("temp.png", picture) #pro použití tesseract je nutné obrázek uložit a znovu nahrát
    output = pytesseract.image_to_string(Image.open("temp.png")) #detekce textu pomocí tesseract
    os.remove("temp.png") #odstraní temp.png

    return output

def prepare(picture):
    #připraví obrázek pro rozpoznání textu
    picture = pic.opening(picture)
    picture = pic.remove_noise(picture)
    picture = pic.get_grayscale(picture)
    picture = pic.erode(picture)
    return picture