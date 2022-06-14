PyGUI aplikace, která je schopná stopovat čas a nastavit budík.

ARDUINO:
1) Arduino IDE
- Náhrát na malý jednodeskový počítač kód, který obsahuje samotný program Arduino IDE
- Soubor>Příklady>Firmata>StandardFirmata
    - Tento kód nám umožní komunikaci s Arduino a především s jeho jednotlivými PINy.
    
2) Python
- Abychom mohli používat Arduino v Pythonu, musíme importovat knihovnu pyfirmata.

3) Programování
- Připojíme Arduino: pyfirmata.Arduino('port')
- Potom můžeme komunikovat s jednotlivými PINy a nastavovat je (vstupní/výstupní).
    - Důležité: připojit jednotlivé součástky na stejné PINy.
    - PIEZZO: PIN č. 9 (důležité PWM)
    - LED: PIN č. 13
    - BUTTON: PIN č. 6

ALARM - BUDÍK:
- Nastavíme čas (hodina, minuta, sekunda), kdy nám budík "zazvoní".
- Pokud nastavený čas = reálnému času, tak se ozve buzzer, který je připojený k desce na Arduino.
- Když buzzer dohraje, tak se budík ukončí a je možné ho nastavit znovu.

STOPWATCH - STOPKY:
- Po stisknutí tlačítka "Start" se sputí stopky.
    - Čas se v reálném čase přepisuje na Labelu, který je vidět na PyGUI.
- Můžeme stopky zastavit, restartovat nebo ukončit celý program.

TODO:
- Stopky spouštět pomocí tlačítka připojeného k Arduino a zobrazovat čas na LCD.
- Rozšířit aplikaci o Timer, který by mohl také komunikovat s Arduino.
- Spusti současně 2 a více nástrojů aplikace.
    - from threading import *

Aplikace obsahuje natavený Buzzer, Led a Button.
Buzzer je funkční, ale Led nebo Button se mi nepodařilo uplatnit v aplikaci.

Problém s rozšiření programu: moje sada Arduino obsahuje malou desku (breadboard) na vytváření větších obvodů.