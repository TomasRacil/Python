"""UserInterface
Modul pro zobrazení detekovaných dat
Vypíše detekovaný string do konzole a zobrazí zadaný obrázek

"""

import cv2 #pro zobrazení obrázku z cv

def ShowResult(pic, text):
    """Zobrazí text do konzole; současně zobrazí okno s obrázkem (vyseknutý MRZ)
    Args:
        pic: obrázek k zobrazení
        text: (string) string k zobrazení do konzole
    Returns:
        upravený obrázek pomocí cv2
    """
    print(text)
    cv2.imshow("MRZ", pic) #zobrazí v okně výsledek
    cv2.waitKey(0)
