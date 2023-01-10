from os.path import join, realpath, dirname

def get_words():
    soubor = open(join(dirname(dirname(realpath(__file__))), "slova.txt"), "r", encoding="utf-8")
    slova = [slovo for slovo in soubor.read().split('\n')]
    return slova
