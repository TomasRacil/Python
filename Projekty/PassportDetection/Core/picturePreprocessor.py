"""PicturePreprocessor
Modul pro zjednodušení a standardizaci práce s obrázky
Máme k dispozici sadu nástrojů pro preprocessing obrázků

"""

import cv2
import numpy as np

def get_grayscale(image):
    """Převede na odstíny šedé barvy
    Args:
        image: obrázek na kterém se provede úprava
    Returns:
        upravený obrázek pomocí cv2
    """
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

def remove_noise(image):
    """Odstraní šum z obrázku
    Args:
        image: obrázek na kterém se provede úprava
    Returns:
        upravený obrázek pomocí cv2 - fce medianBlur
    """
    return cv2.medianBlur(image,1)
 
def thresholding(image):
    """Provede tresholding s parametry (0,255)
    Args:
        image: obrázek na kterém se provede úprava
    Returns:
        převedený obrázek
    """
    return cv2.threshold(image, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]

def opening(image):
    """Provede prvotní operace pro další preprocessing
    Odebere základní šum
    Args:
        image: obrázek na kterém se provede úprava
    Returns:
        obrázek bez šumu
    """
    kernel = np.ones((1,1),np.uint8)
    return cv2.morphologyEx(image, cv2.MORPH_OPEN, kernel)

def canny(image):
    """Převede obrázek na detekované linky (černobílý)
    Args:
        image: obrázek na kterém se provede úprava
    Returns:
        upravený obrázek pomocí cv2
    """
    return cv2.Canny(image, 100, 200)

def get_GaussianBlur(image):
    """Provede lehké rozostření obrázku - může mít vyšší úspěšnost pro Tesseract
    Args:
        image: obrázek na kterém se provede úprava
    Returns:
        obrázek s lehce rozostřenými hranami
    """
    return cv2.GaussianBlur(image, (3, 3), 0)

def erode(image):
    """odebere malé bílé artefakty
       doporučuji najít na webu příklad nebo vyzkoušet
    Args:
        image: obrázek na kterém se provede úprava
    Returns:
        upravený obrázek pomocí cv2
    """
    kernel = np.ones((1,1),np.uint8)
    return cv2.erode(image, kernel, iterations = 1)

def dilate(image):
    """Spojí fragmenty
       doporučuji najít na webu příklad nebo vyzkoušet
    Args:
        image: obrázek na kterém se provede úprava
    Returns:
        upravený obrázek pomocí cv2
    """
    kernel = np.ones((5,5),np.uint8)
    return cv2.dilate(image, kernel, iterations = 1)

