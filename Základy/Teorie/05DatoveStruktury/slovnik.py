#slovník se kterým budeme pracovat
studenti={
	1:{
	"Jméno":"Josef",
	"Příjmení":"Kolík"
	},
	2:{
	"Jméno":"David",
	"Příjmení":"Ryba"
	},
	3:{
	"Jméno":"Ladislav",
	"Příjmení":"Valda"
	}
}

#přístup k jednotlivým prvkům slovníku; také je možno použít metodu get(klíč), která vrací hodnotu klíče předaného argumentem
print(f"První student: {studenti[1]}")
print(f"Jméno druhého studenta: {studenti[2]['Jméno']}\n")

#přidávání nového prvků
studenti['novýKlíč']='nová hodnota'
print(f"Slovník s novou hodnotou: {studenti}\n")

#změna hodnoty
studenti['novýKlíč']='změněná hodnota'
print(f"Slovník se změněnou hodnotou: {studenti}\n")

#pro změnu či přidání prvku je také možno použít metodu update({klíč:hodnota})
studenti.update({'dalšíKlíč':'další nová hodnota'})
print(f"Slovník se další novou hodnotou: {studenti}\n")

#k odstranění prvku používáme metodu pop(klíč)
studenti.pop('novýKlíč')
print(f"Slovník s odstraněným klíčem: {studenti}\n")

#k odstranění posledního prvku používáme metodu popitem()
studenti.popitem()
print(f"Slovník s odstraněným posledním klíčem: {studenti}\n")

#také můžeme využít slova del jako u všech jiných proměných a datových struktur 
#např del studenti[1]


#pokud chceme získat všechny klíče ve slovníku používáme metodu keys() vrací list klíčů
print(f"Klíče slovníku: {studenti.keys()}\n")

#pokud chceme získat všechny hodnoty ve slovníku používáme metodu values() vrací list hodnot
print(f"Hodnoty slovníku: {studenti.values()}\n")

#pro získání jednotlivých dvojic key value používáme metodu items() vrací list n-tic 
#tato metoda je klíčová pokud chceme procházet slovník dvojici po dvojici
print(f"Dvojice hodnota klíč: {studenti.items()}\n")

#operátor in v případě slovníků zjišťuje příslušnost klíče ne hodnoty
print(f"Je novýKlíč v listu: {'novýKlíč' in studenti}\n")

#pokud chceme procházet jednotlivé klíče slovníku použijeme jednoduše for loop a in
print("Klíče slovníku:")
for klic in studenti:
  print(klic)

#pokud chceme procházet jednotlivé hodnoty slovníku použijeme buď opět for loop a nebo metodu values()
print("\nHodnoty slovníku první způsob:")
for klic in studenti:
  print(studenti[klic])

print("\nKHodnoty slovníku druhý způsob:")
for hodnota in studenti.values():
  print(hodnota)

#nejčastěji však použijeme procházení při kterém získáváme jak klíč tak hodnotu
print("\nKlíč hodnota:")
for klic, hodnota in studenti.items():
  print(klic,hodnota)

#pro smazání obsahu celého slovníku můžeme použít metodu clear()
studenti.clear()
print(f"Prázdný slovník: {studenti}\n")

#pokud chceme vytvořit kopii našeho slovníku nemůžeme použít operátor '=' ten by vytvořil jen referenci
#proto používáme metodu copy()
studentiKopie = studenti.copy()
print(f"Prázdný slovník: {studentiKopie}\n")

#pro odstranění slovníku můžeme použít metodu del
del studenti
print(f"Existuje slovník studenti: {'studenti' in vars() or 'studenti' in globals()}\n")