class Datum:
    def __init__(self, rok, mesic, den):
        self.rok = rok
        self.mesic = mesic
        self.den = den

    def __repr__(self) -> str:
        return f"{self.den}.{self.mesic}. {self.rok}"
