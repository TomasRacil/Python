"""PassportDetection
Základní kód programu - příjímá argument (složku s daty)
Obsahuje hlavní loop, který prochází složku a s každým souborem provádí zadané operace - předává je do
jednotlivých knihoven

TODO: další zpracování získaného stringu - detekce dat pomocí regEx
"""

import argparse #parsování argumentu
from imutils import paths #pro paths.list_images
from Core import * #modul s jednotlivými částmi

ap = argparse.ArgumentParser() #přijme argumenty
ap.add_argument("-i", "--images", required=True, help="path to images directory")
args = vars(ap.parse_args())


#hlavní loop - prochází soubory a provádí na nich zadané operace
for cesta in paths.list_images(args["images"]):
	mrzPicture = mrz.process(cesta) #separuje z obrázku MRZ
	mrzPicture = TD.prepare(mrzPicture) #provede úpravu pro lepší rozpoznání textu
	text=TD.recognize(mrzPicture) #rozpozná text na obrázku
	UI.ShowResult(mrzPicture, text) #zobrazí výsledky