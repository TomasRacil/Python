import numpy as np #pro matice
import argparse #parsování argumentů
import imutils #fce resize 
import cv2 #openCV
import os #pro mazání souboru
import pytesseract #OCR pip install tesseract; pip install pytesseract; nutno stáhnout balíček z webu
from PIL import Image #pip install pillow - pro načítání obrázků do tesseract
from imutils import paths #usnadnění práce s opencv (pip install --upgrade imutils)

import Core.picturePreprocessor as pic

rectKernel = cv2.getStructuringElement(cv2.MORPH_RECT, (13, 5))
sqKernel = cv2.getStructuringElement(cv2.MORPH_RECT, (21, 21))

def process(cesta):

    #pomocí imutils prochází složku danou argumentem a hledá obrázky
    data = cv2.imread(cesta) #načte soubor
    data = imutils.resize(data, height=600) #změní výšku na maximálně 600p 
    grayFilter = pic.get_grayscale(data) #zbavíme se barvy - používají se odstíny šedé barvy
    
    grayFilter = pic.get_GaussianBlur(grayFilter) #odstranění šumu pomocí GaussianBlur
    blackhatFilter = cv2.morphologyEx(grayFilter, cv2.MORPH_BLACKHAT, rectKernel) #zvýrazní černou bravu proti světlému pozadí - zvýrazní text
    
    #Sobel operator - výpočet gradientů - zde jsem musel použít kód z webu 
    gradX = cv2.Sobel(blackhatFilter, ddepth=cv2.CV_32F, dx=1, dy=0, ksize=-1)
    gradX = np.absolute(gradX)
    (minVal, maxVal) = (np.min(gradX), np.max(gradX))
    gradX = (255 * ((gradX - minVal) / (maxVal - minVal))).astype("uint8")
    
    gradX = cv2.morphologyEx(gradX, cv2.MORPH_CLOSE, rectKernel) #vyplní se prázdná místa mezi jednotlivými znaky - vytvoří oblasti, které
    															# by mohly být řádky
    thresh = pic.thresholding(gradX)
    thresh = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, sqKernel) #detekce řádků - spojí je do jedné oblasti
    thresh = cv2.erode(thresh, None, iterations=4) #odstraní se oblasti, které jsou moc malé na to, aby mohly být MRZ
    
    p = int(data.shape[1] * 0.05) #z oblastí označených jako řádky se odstraní na každé straně 5% pixelů - pro vyloučení chyby
    thresh[:, 0:p] = 0
    thresh[:, data.shape[1] - p:] = 0
    
    #na obrázku máme několik velkých zvýrazněných oblastí - musíme najít MRZ - je to obdélníková oblast, která bude mít téměř konstantní poměr stran
    oblasti = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE) #vyhledá všechny oblasti
    oblasti = imutils.grab_contours(oblasti) #vezme pouze vyhledané oblasti
    oblasti = sorted(oblasti, key=cv2.contourArea, reverse=True) #setřídí je podle velikosti - nejvetší oblast je na prvním místě
    
    #prochází v loopu každou oblast a počítá poměr stran a orovná velikost oblasti vůči původnímu obrázku
    for oblast in oblasti:
    	(x, y, w, h) = cv2.boundingRect(oblast)
    	ar = w / float(h)
    	crWidth = w / float(grayFilter.shape[1])
    
    	if ar > 5 and crWidth > 0.75:
    		pX = int((x + w) * 0.03) #souřadnice x MRZ
    		pY = int((y + h) * 0.03) #souřadnice y MRZ
    		(x, y) = (x - pX, y - pY)
    		(w, h) = (w + (pX * 2), h + (pY * 2))
    		vysledek = data[y:y + h, x:x + w].copy()
    		cv2.rectangle(data, (x, y), (x + w, y + h), (0, 255, 0), 2)
    		break

    return vysledek
