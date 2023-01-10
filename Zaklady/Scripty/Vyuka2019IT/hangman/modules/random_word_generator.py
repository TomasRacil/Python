from random import randrange

from .file_reader import get_words

def get_random_word():
    slova = get_words()
    delka_slov=len(slova)
    index_nahodneho_slova= randrange(delka_slov)
    return slova[index_nahodneho_slova].lower()