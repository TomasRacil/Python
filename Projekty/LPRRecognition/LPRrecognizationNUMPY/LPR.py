import cv2
import imutils
import numpy as np
import pytesseract
#pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files (x86)\Tesseract-OCR\tesseract.exe'

img = cv2.imread('spz\\SA.jpg',cv2.IMREAD_COLOR)
img = cv2.resize(img, (600,400) )

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) 
gray = cv2.bilateralFilter(gray, 13, 15, 15) 		###zbavení se šumu

edged = cv2.Canny(gray, 30, 220) 				#vykreslení hran
#cv2.imshow('hrany',edged)	#kontorla

### HLEDANI spojenych hran ###
contours = cv2.findContours(edged.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
#print(contours)	#kontorla listu
contours = imutils.grab_contours(contours)
contours = sorted(contours, key = cv2.contourArea, reverse = True)[:10]	#uspořádání od největšího pouze prvnich deseti prvku, zbytek ignorujeme
#print(contours)	#kontorla listu
screenCnt = None

for c in contours:			#v cyklu najdeme ktery ze spojenych objektu ma tvar obdelniku (4 propojene strany a uzavřený tvar)
    #hledáme přibližný obrys
    peri = cv2.arcLength(c, True)			
    approx = cv2.approxPolyDP(c, 0.018 * peri, True)
 
    if len(approx) == 4:	#Pokud má přibližný obrys 4 body předpokládáme, že jsme našli SPZ a uložíme do screenCnt
        screenCnt = approx
        break

if screenCnt is None:		#Pokud není nalezen obrys se 4 body
    detected = 0
    print ("No contour detected")
else:
     detected = 1

if detected == 1:			#Vykreslíme okolo nalezeného obrysu obdelník, pro ujištění se že je to SPZ 
    cv2.drawContours(img, [screenCnt], -1, (0, 0, 255), 3)

maska = np.zeros(gray.shape,np.uint8)	#vytvoření masky okolo nalezené SPZ
new_image = cv2.drawContours(maska,[screenCnt],0,255,-1,)
new_image = cv2.bitwise_and(img,img,mask=maska)
#cv2.imshow('maska',new_image)	#kontrola

(x, y) = np.where(maska == 255)	#Oriznuti obrazku kde je maska
(topx, topy) = (np.min(x), np.min(y))
(bottomx, bottomy) = (np.max(x), np.max(y))
Cropped = gray[topx:bottomx+1, topy:bottomy+1]
#cv2.imshow('oriznute',Cropped)	#kontrola

### znovu vykresleni hran textu (navic- neni potreba) ###
#edged2 = cv2.Canny(Cropped, 30, 220) 
#cv2.imshow('2prevod',edged2)	#kontrola
###													  ###

### Cteni textu z vysledneho obrazku ###
#print(pytesseract.get_languages(config=''))	#kontrola dostupnych nastaveni teseracu (lang=...)

text = pytesseract.image_to_string(Cropped, lang='eng', config='--psm 10')	#config --psm10 je single character recognition (moznosti nastaveni --psm lze najit napsanim do konzole "tesseract --help-psm") mozno dodat --oem 1 (Neural Nets) 
print("License Plate Recognition (LPR)\n")
print("SPZ auta:",text)
img = cv2.resize(img,(500,300))
Cropped = cv2.resize(Cropped,(400,200))		#zvetseni oriznuteho vysledku
cv2.imshow('original',img)	#original
cv2.imshow('vysledek',Cropped)	#vysledek SPZ

cv2.waitKey(0)
cv2.destroyAllWindows()