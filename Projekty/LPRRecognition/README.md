Projekt pro rozpoznávání SPZ v OpenCV
=====================================

### TODO:
1. #### Seznámení se s jazykem Python a knihovnou OpenCV.
   - instalace OpenCV a následné propojení s projektem.

2. #### Inspirace podle projektu na [Git.](https://github.com/MicrocontrollersAndMore/OpenCV_3_License_Plate_Recognition_Python.git)

3. #### Vytvoření si podprogramu "strojového učení čtení znaků". Zvolíme vlastní fonty, které se nejčastěji používají na SPZ.
   - vygenerování .txt souborou, které budou použity k rozpoznávání SPZ

4. #### Samotný program na rozeznání SPZ:
   - Nalezení značky
   - Převod obrázku na černobílý (ze začátku převod z obrázku, v pokrořilejší fázi převod z videa)
   - Nalezení možných znaků v obrázku
   - Vytvoření vektoru možných znaků, které jsou u sebe a mohou tvořit SPZ
   - Vyjmutí vektoru možných znaků z obrázku a uložení do listu
   - Zvětšení a zaměření se na listy kde se vyskytují znaky
   - Znovu převod obrázku na černobílý
   - Rozpoznání znaků na značce
   - Vybrání značky, která má buď nejvíce možných znaků nebo určitý standardizovaný počet znaků
   - Vyjmutí této značky z listu a porovnání se znaky
   - Poté ukázání výsledku ve formě okna a znaků pod ním napsaných + vypsané nebo zapsání do databáze

> //*Možné rozepsání kroků a připsání některých chybějících, nebo v případě naražení na další problémy, možnost rozepsat*//


Autoři: [@EditaBozkova](https://github.com/EditaBozkova), [@Lubos-source](https://github.com/Lubos-source), [@Pompino](https://github.com/Pompino)
