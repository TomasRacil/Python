import cv2 #pro zobrazení obrázku z cv

def ShowResult(pic, text):
    print(text)
    cv2.imshow("MRZ", pic) #zobrazí v okně výsledek
    cv2.waitKey(0)
