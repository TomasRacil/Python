"""
Iterátory jsme již mohli vidět, když jsme pracovali s datovými strukturami a řetězci. 
Iterátory jsou totiž objekty, kterými je možné procházet prvek po prvku (např. znak po znaku u řetezců)
Ovšem iterátory jsme schopní i vytvářet. 
Obecně se dá říct že vytvořit vlastní generátor je lepší než vytvářet vlastní iterovatelnou třídu, 
ale mohou nastat situace, kde může být tato znalost užitečná.
"""
#JAk bylo možná vidět v předchozích kapitolách řetězce, lity apod. 
#jsme schopní procházet prvek po prvku využitéím cyklu a vrazu in
ukazka="Ukázka"

print("Procházení řetězce prvek po prvku cyklem for: ")
for znak in ukazka:
	print(znak)

#Ovšem toto řešení nám nepomůže v případe, že bychom chtěli přečíst prvek, pokračovat v porgramu
#a následně se vrátit k iterátoru a přečíst další prvek 

#Proto využijeme speciální metody pro vyvolání třídy jako iterátoru
iterarotRetezceUkazka=iter(ukazka)
print(f"\nPrvní znak v řetězci: {next(iterarotRetezceUkazka)}")
print("Zde může proběhnout jakákoliv operace a když se znovu vrátíme k iterátoru budeme tam kde jsme skončili")
print(f"Druhý znak v řetězci: {next(iterarotRetezceUkazka)}")
print(f"Třetí znak v řetězci: {next(iterarotRetezceUkazka)}")


#Ukázka jednoduché iterovatelné třídy.
class NekonecnyIterator:
    """Nekonecny iterator lichých čísel"""

    def __iter__(self):
        self.cislo = 1
        return self

    def __next__(self):
        cislo = self.cislo
        self.cislo += 2
        return cislo

#Vytvoření instance iterátorovatelné třídy
nekIter = iter(NekonecnyIterator())

#Volání jednotlivých prvků iterovatelné třídy
print(f"\nPrvní prvek naší iterovatelné třídy: {next(nekIter)}")
print(f"Druhý prvek naší iterovatelné třídy: {next(nekIter)}")
print(f"Třetí prvek naší iterovatelné třídy: {next(nekIter)}")