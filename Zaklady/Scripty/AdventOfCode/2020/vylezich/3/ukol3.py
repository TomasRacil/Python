soubor = open("3.txt", "r").readlines()
pocetStromu = 0
start = 0
"""Prochazeni celého souboru a hledání, #"""
for radek in soubor:
    if(radek[start]=='#'):
        pocetStromu = pocetStromu+1
        """Podmínky pro průchod námi chtěné cesty a znovunastaevení"""
    if(start==28):
        start = -3
    if(start==29):
        start = -2
    if(start==30):
        start = -1
    start = start + 3
    """Výsledný počet stromů"""

    """Autorské řešení:"""
print(f"Pocet stromu po tomhle cyklu je: {pocetStromu}")