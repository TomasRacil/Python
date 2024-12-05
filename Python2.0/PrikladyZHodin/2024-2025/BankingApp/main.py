from __future__ import annotations
from Banka import Datum, Transakce, Ucet


class Banka:
    def __init__(self, transakce):
        self.transakce = transakce

    def __repr__(self) -> str:
        return ""


if __name__ == "__main__":
    datum = Datum(2024, 11, 28, 12)
    transakce = Transakce(1, 2, 3, datum)
    transakce1 = Transakce(1, 2, 3, datum)
    ucet = Ucet(1, [transakce, transakce1])
    ucet.spocitej_stav()
    print(ucet)
