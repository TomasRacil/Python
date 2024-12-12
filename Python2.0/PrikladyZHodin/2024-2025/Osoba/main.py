from __future__ import annotations
from os.path import join, realpath, dirname
import random


class Osoba:
    def __init__(self, jmeno, prijmeni, vek, cislo_op=None):
        self.jmeno = jmeno
        self.prijmeni = prijmeni
        self.vek = vek
        self.cislo_op = cislo_op if cislo_op else self.generujCisloOP()

    @classmethod
    def vytvorOsobuZTXT(cls, cesta) -> Osoba:
        with open(cesta) as f:
            data = [
                int(zaznam) if zaznam.isdigit() else zaznam
                for zaznam in f.read().split(";")
            ]
            return Osoba(*data)

    @staticmethod
    def generujCisloOP() -> int:
        return random.randrange(99999, 1000000)

    @property
    def vek(self):
        return self._vek

    @vek.setter
    def vek(self, hodnota):
        if 0 < hodnota < 150:
            self._vek = hodnota
        else:
            raise ValueError("Neplatna hodnota veku")

    @property
    def cislo_op(self):
        return self._cislo_op

    @cislo_op.setter
    def cislo_op(self, hodnota):
        if 99999 < hodnota < 1000000:
            self._cislo_op = hodnota
        else:
            raise ValueError("Neplatna hodnota op")

    def zkontorlujPlatnostJmena(func):
        def wrapper(self):
            if len(self.jmeno) > 0 and len(self.prijmeni) > 0:
                func(self)

        return wrapper

    @zkontorlujPlatnostJmena
    def pozdrav(self):
        print(f"Ahoj {self.jmeno} {self.prijmeni}")

    def __str__(self):
        return f"{self.jmeno} {self.prijmeni} {self.vek} let c. op {self.cislo_op}"


if __name__ == "__main__":
    osoba = Osoba("", "Novy", 1)
    print(osoba)
    osoba.pozdrav()

    osoba2 = Osoba.vytvorOsobuZTXT(join(dirname(realpath(__file__)), "osoba.txt"))
    print(osoba2)
    osoba2.pozdrav()
