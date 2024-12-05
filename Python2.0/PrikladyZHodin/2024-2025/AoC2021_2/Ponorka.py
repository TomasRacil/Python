class Ponorka:
    def __init__(self):
        self.horizontalni = 0
        self.hloubka = 0

    def naviguj(self, prikaz: str) -> None:
        prikaz = prikaz.split()
        match (prikaz[0]):
            case "forward":
                self.horizontalni += int(prikaz[1])
            case "up":
                self.hloubka -= int(prikaz[1])
            case "down":
                self.hloubka += int(prikaz[1])
            case _:
                pass

    def vysledek(self) -> int:
        return self.hloubka * self.horizontalni
