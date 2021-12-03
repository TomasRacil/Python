#spotreba=3

class Vozidlo:
    pocetKol = None
    spotreba = None #l/100km

    def __init__(self, spotreba, pocKol=4):
        self.pocetKol=pocKol
        self.spotreba=spotreba
    
    def spotrebaMPG(self):
        return f"Spotreba v mpg je: {235.215/self.spotreba}"

class Motorka(Vozidlo):
    def __init__(self, spotreba):
        super().__init__(spotreba, pocKol=2)

mojeAuto=Vozidlo(8)
tvojeAuto=Vozidlo(12,6)
mojeMotorka=Motorka(4)

print(mojeAuto.pocetKol,mojeAuto.spotreba, mojeAuto.spotrebaMPG())
print(tvojeAuto.pocetKol,tvojeAuto.spotreba)
print(mojeMotorka.pocetKol,mojeMotorka.spotreba, mojeMotorka.spotrebaMPG())

# mojeAuto.pocetKol=6

# print(mojeAuto.pocetKol)