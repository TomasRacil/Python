"""TextDetection
Modul pro detekci textu v zadaném obrázku

TODO: Vyřešit předání obrázku v rámci operační paměti - aby se nemusel ukládat na disk
"""

import cv2 #openCV
import os #pro mazání souboru
import pytesseract #OCR pip install tesseract; pip install pytesseract; nutno stáhnout balíček z webu
from PIL import Image #pip install pillow - pro načítání obrázků do tesseract
import Core.picturePreprocessor as pic

pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files/Tesseract-OCR/tesseract' #cesta k nainstalovanému tesseract

def recognize(picture):	
    """Rozpozná text na zadaném obrázku pomocí tesseract
    Args:
        image: obrázek se separovaným MRZ
    Returns:
        output: (string) detekovaný text pomocí tesseract
    """
    cv2.imwrite("temp.png", picture) #pro použití tesseract je nutné obrázek uložit a znovu nahrát
    output = pytesseract.image_to_string(Image.open("temp.png")) #detekce textu pomocí tesseract
    os.remove("temp.png") #odstraní temp.png

    return output


def prepare(picture):
    """Připraví obrázek na rozpoznání textu - provede na něm základní úpravy
    Args:
        picture: vstup pro úpravu
    Returns:
        picture: upravený obrázek pomocí cv2 - připravený na předání do fce recognize
    """

    picture = pic.opening(picture)
    picture = pic.remove_noise(picture)
    picture = pic.get_grayscale(picture)
    picture = pic.erode(picture)
    return picture