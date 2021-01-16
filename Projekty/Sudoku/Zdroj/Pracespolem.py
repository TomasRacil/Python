from random import randint, shuffle
cislaSeznam = [1, 2, 3, 4, 5, 6, 7, 8, 9]
counter = 0 # počítá počet řešní

def obtiznostNastav():
    """obtiznostNastav --- Funkce nastavujicí pocatecni obtiznost a kontrolující, zda-li uživatel zadal správné číslo
    Args:
        obtiznost --- uroven obtiznosti
    :returns: obtiznost
    """
    print("V případě zájmu udělejte prosím výstřižek sudoku")
    obtiznost = int(input("Zadejte obtiznost (1-3): \n"))
    if (obtiznost > 3):
        print(f"Zvolili jste spatnou obtiznost")
    elif (obtiznost < 1):
        print(f"Zvolili jste spatnou obtiznost")
    return obtiznost

def konzole(bod):
    """konzole --- Funkce vypisující v konzoli pomocí for cyklu a print - celé sudoku
    Args:
        bod --- list, dvourozměrné pole
    Returns:
        Graficky znázorněné sudoku v konzoli"""
    print("Sudoku bod Ready")
    for sloupec in range(0, 9):
        print(
            f"{bod[sloupec][0]} {bod[sloupec][1]} {bod[sloupec][2]} | {bod[sloupec][3]} {bod[sloupec][4]} {bod[sloupec][5]} | {bod[sloupec][6]} {bod[sloupec][7]} {bod[sloupec][8]}")
        if (sloupec % 3 == 2):
            print("_____________________")

def checkBod(bod):
    """checkBod --- Kontroluje výskyt prvku v řádku a
    Args:
        bod --- list, dvourozměrné pole
    Returns:
        bool:  True, False"""
    for rad in range(0, 9):
        for slo in range(0, 9):
            if bod[rad][slo] == 0:
                return False
    return True


def praceBod(bod, varianta):
    """praceBod --- Tato funkce slouží k naplnění sudoku a funkce k řešení sudoku, je toho dosáhnuto pomocí parametrů:
    je zde zvolena rekurzivně, tedy pokud nejsou splněny počáteční podmínky, je volána znovu
    Args:
        bod --- list, dvourozměrné pole
        varianta --- v programu určí, která z variant bude použita, zdali
                    1 - pro kontrolu, pracuje s globální proměnnou counter, která řeší počet řešení
                    2 - pro naplnění a kontrolu, zda
                    counter --- počítá počet řešení
    Returns:
        1 --- counter+=1
        2 --- True
        """
    global counter
    for i in range(0, 81):
        rad = i // 9 # klasické dělení
        slo = i % 9 # modulo, zbytek po dělení, takže postupně budou hodnoty 1,2,3
        if bod[rad][slo] == 0:
            """Míchá seznam, aby nedocházelo k 1234.."""
            shuffle(cislaSeznam)
            for value in (cislaSeznam):
                if not (value in bod[rad]): #kontroluje jestli je v radku
                    """Kontroluje, zdali jsou hodnoty v jednotlivých sloupcíh, místo výpisu po prvcích jsem zvolil tuhle kontrolu cyklem"""
                    if not value in (bod[n][slo] for n in range(0, 8)):
                        square = []
                        """Kontroluje, v jakém čtverci se pohybujeme, pro kontrolu, jestli číslo již není použito"""
                        if rad < 3:
                            if slo < 3:
                                square = [bod[i][0:3] for i in range(0, 3)]
                            elif slo < 6:
                                square = [bod[i][3:6] for i in range(0, 3)]
                            else:
                                square = [bod[i][6:9] for i in range(0, 3)]
                        elif rad < 6:
                            if slo < 3:
                                square = [bod[i][0:3] for i in range(3, 6)]
                            elif slo < 6:
                                square = [bod[i][3:6] for i in range(3, 6)]
                            else:
                                square = [bod[i][6:9] for i in range(3, 6)]
                        else:
                            if slo < 3:
                                square = [bod[i][0:3] for i in range(6, 9)]
                            elif slo < 6:
                                square = [bod[i][3:6] for i in range(6, 9)]
                            else:
                                square = [bod[i][6:9] for i in range(6, 9)]
                        if not value in (square[0] + square[1] + square[2]):
                            """Samotné rozdělení variant, pro jednu funkci, která pracuje s bodem"""
                            if(varianta==1):
                                bod[rad][slo] = value
                                if checkBod(bod):
                                    counter += 1
                                    break
                                else:
                                    if praceBod(bod,varianta):
                                        return True
                            else:
                                bod[rad][slo] = value
                                if checkBod(bod):
                                    return True
                                else:
                                    if praceBod(bod,varianta):
                                        return True
            break
    bod[rad][slo] = 0

def vymazBod(bod, obtiznost):
    """vymazBod --- Funkce, která z naplněného sudoku postupně maže jednotlivé prvky a zároveň kontroluje, aby bylo možné právě 1 řešení
    pomocí funkce praceBod(), s parametrem 1 - tedy kontrola řešení sudoku
    Args:
        bod --- list, dvourozměrné pole
        obtiznost --- int, přebírá číslo pro další úpravy
        copybod --- list, zkopírování bodu, pro kontrolu počtu řešení
    Returns:
        """
    pokusy=20+obtiznost*10
    while pokusy > 0:
        """vybírám jednotlivá náhodná políčka"""
        rad = randint(0, 8)
        slo = randint(0, 8)
        while bod[rad][slo] == 0:
            rad = randint(0, 8)
            slo = randint(0, 8)
        backup = bod[rad][slo]
        bod[rad][slo] = 0
        copybod = []
        for r in range(0, 9):
            copybod.append([])
            for c in range(0, 9):
                copybod[r].append(bod[r][c])
        """Zde dochází ke kontrolej jednoho řešení"""
        praceBod(copybod,1)
        if counter != 1:
            pokusy -= 1

