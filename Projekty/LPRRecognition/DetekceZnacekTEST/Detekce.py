import cv2

#import pytesseract

################## NASTAVENI pevnych promenych ###########################
frameWidth = 640
frameHeight = 480
nPlateCascade = cv2.CascadeClassifier("haarcascades/haarcascade_russian_plate_number.xml")	#stazeny xml soubor z netu pro urceni co je SPZ (ruska)
minArea = 200
color = (255,0,255)
###############################################

cap = cv2.VideoCapture(0)	#zaznam kamery (0 - defaultni id)
cap.set(3, frameWidth)
cap.set(4, frameHeight)
cap.set(10,100)
count = 0

while True:
	success, img = cap.read()
	imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)		#prevod na GRAY
	numberPlates = nPlateCascade.detectMultiScale(imgGray, 1.1, 10)	#detekovani SPZ pomoci XML a Gray obr.
	for (x, y, w, h) in numberPlates:
		area = w*h
		if area >minArea:
			cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 255), 2)	#vykresleni obdelniku okolo SPZ
			cv2.putText(img,"Number Plate",(x,y-5),cv2.FONT_HERSHEY_COMPLEX_SMALL,1,color,2)	#Napsani textu nad obdelnik
			imgCropped = img[y:y+h,x:x+w]	#oriznuti obdelniku (SPZ)
			cv2.imshow("Oriz",imgCropped)	#zobrazeni SPZ v okne "Oriz"
			

			#TEST tesseract #text=pytesseract.image_to_string(imgCropped,lang="eng")
			#print(text)


	cv2.imshow("Vysledek", img)	#zobrazeni zaznamu z webky + obdelnik + text (v okne "vysledek" )

	""" Zatim nefunguje ukladani (zjistiji proc) """
	if cv2.waitKey(1) and 0xFF == ord('s'):
		cv2.imwrite('Scanned/NoPlate_'+str(count)+'.jpg',imgCropped)	#ulozi oriznutou znacku do slozky
		cv2.rectangle(img,(0,200),(640,300),(0,255,0),cv2.FILLED)	#zeleny vyplneny obdelnik
		cv2.putText(img,"Scan Saved",(150,265),cv2.FONT_HERSHEY_DUPLEX,2,(0,0,255),2)	#text scan ulozen na zelenem obdelniku
		cv2.imshow("Vysledek",img)	#prekresleni okna "Vysledek" s textem + zeleny obdelnik pres okno
		cv2.waitKey(1000)	#pocka 1 sec a zase zobrazi okno bez prekresleneho obdelniku Scane ulozen
		count +=1
