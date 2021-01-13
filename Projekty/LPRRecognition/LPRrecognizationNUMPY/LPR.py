import cv2
import imutils
import numpy as np
import pytesseract
#pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files (x86)\Tesseract-OCR\tesseract.exe'

img = cv2.imread('spz\\SA.jpg')                                                                                                                          #(,cv2.IMREAD_COLOR)
"""
Definování cesty k obrázku
""" 

img = cv2.resize(img, (600,400) )
"""
Změna velikosti a uložení do proměnné img
Změnou velikosti zabráníme problémům s velkým rozlišením fotografií
"""

cv2.imshow('Orig',img)	#kontrola 
"""
Zobrazení obrázku v okně
"""


gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) 
"""
Převedení obrázku do odstínů šedé
Obrázek v odstíněch šedé zrychlí další kroky
"""

gray = cv2.bilateralFilter(gray, 13, 15, 15) 		
"""
Zbavení se šumu a nedostatků fotky
Můžeme nastavovat 2 poslední parametry od 15 výš - podle toho se rozmaže pozadí
"""

#cv2.imshow('Gray',gray)	#kontrola


edged = cv2.Canny(gray, 30, 220) 				
"""
Vykreslení hran na obrázku

    Args:
        (int): minimum a maximum 
        hrany které mají "intensity gradient" mezi těmito
        hodnotami se vykreslí
"""

cv2.imshow('hrany',edged)	#kontrola


                        ##### hledaní spojených hran #####

contours = cv2.findContours(edged.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)                                                                 #cv2.findContours(edged.copy(), cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
"""
Najdeme uzavřené obrysy, abychom lépe detekovali všechny obdélníky na obrázku
a z nich vybrali SPZ
"""

#print(contours)	#kontrola listu

contours = imutils.grab_contours(contours)
"""
Obrysy uchováme
"""

contours = sorted(contours, key = cv2.contourArea, reverse = True)[:10]	
"""
Uspořádáme od největšího a uchováme prvních 10 prvků
"""

#print(contours)	#kontrola listu

screenCnt = None

for c in contours:			
"""
Projdeme všechny obrysy a najdeme takový, který má tvar obdélníku,
4 strany a je uzavřený.
"""

    peri = cv2.arcLength(c, True)			
    approx = cv2.approxPolyDP(c, 0.018 * peri, True)
 
    if len(approx) == 4:	                                                                                                                               #Pokud má přibližný obrys 4 body předpokládáme, že jsme našli SPZ a uložíme do screenCnt
        screenCnt = approx
        break

if screenCnt is None:		                                                                                                                                 #Pokud není nalezen obrys se 4 body
    detected = 0
    print ("No contour detected")
else:
     detected = 1

if detected == 1:			                                                                                                                                 #Vykreslíme okolo nalezeného obrysu obdelník, pro ujištění se že je to SPZ 
    cv2.drawContours(img, [screenCnt], -1, (0, 0, 255), 3)
    """
    Okolo nalezeného obdélníku vykreslíme červený tvar
    """

                            ##### Vytvoření masky okolo nalezené SPZ #####
maska = np.zeros(gray.shape,np.uint8)	
new_image = cv2.drawContours(maska,[screenCnt],0,255,-1,)
new_image = cv2.bitwise_and(img,img,mask=maska)
"""
Vytvoříme masku okolo nalezené SPZ a zbytek obrázku odstraníme
"""

#cv2.imshow('maska',new_image)	#kontrola

                            ##### Oriznuti obrazku, kde je maska #####
(x, y) = np.where(maska == 255)	
(topx, topy) = (np.min(x), np.min(y))
(bottomx, bottomy) = (np.max(x), np.max(y))
Cropped = gray[topx:bottomx+1, topy:bottomy+1]
"""
Ořízneme obrázek, pomocí masky
"""

#cv2.imshow('oriznute',Cropped)	#kontrola


                            ##### Cteni textu z vysledneho obrazku #####

#print(pytesseract.get_languages(config=''))	                                                                                                                      #kontrola dostupnych nastaveni teseracu (lang=...)

text = pytesseract.image_to_string(Cropped, lang='eng', config='--psm 10')	                                                                                         #config --psm10 je single character recognition (moznosti nastaveni --psm lze najit napsanim do konzole "tesseract --help-psm") mozno dodat --oem 1 (Neural Nets) 
"""
Použijeme tesseract na přečtení textu z obrázku

    Args:
        lang (str): jazyk
        config (str): --psm10 je single character recognization
        hrany které mají "intensity gradient" mezi těmito
        hodnotami se vykreslí
"""

print("License Plate Recognition (LPR)\n")
print("SPZ auta:",text)
"""
Zobrazení výsledného převodu textu z obrázku
"""

img = cv2.resize(img,(500,300))
Cropped = cv2.resize(Cropped,(400,200))
"""
Zvětšení oříznutého obrázku
"""

cv2.imshow('original',img)
"""
Zobrazí originál
"""

cv2.imshow('vysledek',Cropped)	
"""
Zobrazí oříznutý výsledek
"""

cv2.waitKey(0)
"""
Neukončí program po dokončení operací
"""

cv2.destroyAllWindows()
"""
Zničí všechny okna
"""


##### Nápověda k nastavení #####

""" TESSERACT nastaveni
def build_tesseract_options( psm=7):
    # tell Tesseract to only OCR alphanumeric characters
    alphanumeric = "ABCDEFHIJKLMNPRSTUVXYZ0123456789"
    options = "-c tessedit_char_whitelist={}".format(alphanumeric)
    # set the PSM mode
    options += " --psm {}".format(psm)
    # return the built options string
    return options
"""

"""
morphology - mozne vyuzit - krasne vykresluje kontrast
rectKernel = cv2.getStructuringElement(cv2.MORPH_RECT, (13, 5))     ###cisla (13,5) meni toleranci ?
blackhat = cv2.morphologyEx(gray, cv2.MORPH_BLACKHAT, rectKernel)
cv2.imshow('BlackHat',blackhat)   #kontorla
"""