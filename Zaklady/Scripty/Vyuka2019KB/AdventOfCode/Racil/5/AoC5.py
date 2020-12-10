#vytváříme set letenek letenky musí být jedinečné proto je set ideální
letenky={
int("".join(["0" if char=="F" else "1" for char in letenka.strip()[:-3]]),2) #procházíme každý znak a vytváříme list nul a jedniček (F=0,B=1), následně tento list spojíme v řetězec a tento řetězec pomocí castingu převedeme na int int(str,2)  dva označuje že řetězec obsahuje číslo v binární formě
*8 #vynásobíme získané binární číslo osmi
+int("".join(["0" if char=="L" else "1" for char in letenka.strip()[-3:]]),2) #podobné jako u prvního akorát L=0 R=1
for letenka in open("letenky.txt", "r")} #procházíme soubor řádek po řádku
#v setu máme pak uložené všechny letenky s jejich čísly převedenými z do desítkové soustavy

#maximální hodnota v setu max()
print(max(letenky))

#vytvoříme set pomocí castingu a generátoru s rozsahem od nejnižší po nejvyšší letenku
#následně uděláme rozdíle mezi tímto setem a letnkami tak se nám vrátí jediný prvek
#abychom získali hodnotu kterou tento set obsahuje změníme ho na iterátor iter() a zavolám první element pomocí next()
print(next(iter((set(range(min(letenky),max(letenky)))-letenky))))