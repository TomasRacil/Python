## Projekt pro rozpoznávání SPZ v OpenCV

TODO:
1)	Seznámení se s jazykem Python a knihovnou OpenCV.
	-instalace OpenCV a propojení s projektem.

2)	Inspirace podle projektu na Git : "https://github.com/MicrocontrollersAndMore/OpenCV_3_License_Plate_Recognition_Python?fbclid=IwAR1T5z2nZTCi4HFX0SVd_A_QxJEiinoNS_uQmzagPfS2m3M1_H_GmHAhSZ8"

3)	Vytvoøení si podprogramu "strojového uèení ètení znakù". Zvolíme vlastní fonty, které se nejèastìji používají na SPZ.
	-vygenerování .txt souborou, které budou použity k rozpoznávání SPZ

4)	Samotný program na rozeznání SPZ:
	Nalezení znaèky
	-Pøevod obrázku na èernobílý
	-Nalezení možných znakù v obrázku
	-Vytvoøení vektoru možných znakù, které jsou u sebe a mohou tvoøit SPZ
	-Vyjmutí vektoru možných znakù z obrázku a uložení do listu
	-Zvìtšení a zamìøení se na listy kde se vyskytují znaky
	-Znovu pøevod obrázku na èernobílý
	-Rozpoznání znakù na znaèce
	-Vybrání znaèky, která má buï nejvíce možných znakù nebo urèitý standardizovaný poèet znakù
	-Vyjmutí této znaèky z listu a porovnání se znaky
	-Poté ukázání výsledku ve formì okna a znakù pod ním napsaných + vypsané

//*Možné rozepsání krokù a pøipsání nìkterých chybìjících, nebo v pøípadì naražení na další problémy, možnost rozepsat*//


Autoøi: des. Edita Božková, des. Daniel Popeláø, des. Lubomír Horký
