from os import path


def zakoduj(strom, cesta, kodovani):
    if type(strom[0]) is int and type(strom[1]) is str:
        kodovani[strom[1]] = cesta
    else:
        zakoduj(strom[1][0], cesta + "0", kodovani)
        zakoduj(strom[1][1], cesta + "1", kodovani)


with open(path.join(path.dirname(path.realpath(__file__)), "test.txt")) as soubor:
    text = soubor.read()
    # text = "BCAADDDCCACACAC"
    frekvence_znaku = sorted(
        [(znak, text.count(znak)) for znak in set(znak for znak in text)],
        key=lambda x: x[1],
    )
    print(frekvence_znaku)
    strom = (frekvence_znaku[0][1], frekvence_znaku[0][0])
    for znak, frekvence in frekvence_znaku[1:]:
        strom = (
            strom[0] + frekvence,
            tuple(sorted([strom, (frekvence, znak)], key=lambda x: x[0])),
        )

    kodovani = {}
    zakoduj(strom, "", kodovani)

    print(kodovani)
