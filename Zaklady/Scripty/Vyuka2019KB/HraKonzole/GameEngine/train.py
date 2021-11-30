from GameEngine import *

def train(self):
    hod=hodKostkou(1,6)
    print("\nHodil jsi: " + str(hod) + "\n")   

    if hod == 1:
        print("Promrhal si celý den. Nechtěl jsi náhodou trénovat?\nZískáváš 0 xp.")

    elif hod == 2:
        print("Zkusil sis rychle zacvičit. A stejně rychle tě to přešlo.\nZískáváš 10 xp.")
        self.xp = self.xp + 10

    elif hod == 3 or hod == 4:
        print("Přečetl jsi půlku manuálu pro dobrodruhy.\nZískáváš 30 xp.")
        self.xp= self.xp + 30

    elif hod == 5:
        print("Přemluvil jsi náhodného kolemjdoucího na sparring. Snad to ještě někdy rozchodí...\nZískáváš 60 xp.")
        self.xp = self.xp + 60

    elif hod == 6:
        print("DING!\nZískáváš level.")
        self.lvl = self.lvl + 1