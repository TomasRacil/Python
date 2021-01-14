Tkinter nebo PyGUI aplikace, která bude schopná stopovat čas, nastavit časovač a budík se zvukem. 


TODO:
- Importování modulu Tkinter nebo PyGUI:
	from tkinter import *

- Základní nastavení prametrů dialogového okna:
	dialog = Tk()			// definování proměnné dialog
	dialog.title('stopwatch, alarm clock, timer')	// název dialogového okna
	dialog.gemoetry ("400x200")		// nastavení rozlišení dialogového okna

- Vytvoření textového pole:
	label = Label(dialog, text = "time") 

- Vytvoření funkce, která nám uloží do proměnných (hodinu, minutu, sekundu):

	def time ():
		hour = time.strftime("%H")		// funkce strftime
		minute = time.strftime("%M")
		sec = time.strftime("%S")
	
	label.config(text=hour + ":" + minute + ":" + second)

Chyby v programu k opravě: 
	1. stopwatch - po zastaveni a opetovnem stisknuti tlacitka start se nic nestane
	2. timer - musi se zadat vsechny hodnoty pred spustenim
	3. alarm - po nastaveni casu se aplikace zastavi a zvukove upozorneni se ozve az kdyz vyprsi cas

