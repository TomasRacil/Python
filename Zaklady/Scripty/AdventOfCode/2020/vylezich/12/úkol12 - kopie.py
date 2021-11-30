"""12. úkol - hodina - Waypoint :("""
class Waypoint:
    rotace = 90
    poziceWN = 1
    poziceWE = 10
    poziceN = 0
    poziceE = 0
    pomocna = 0

    def orientace(self, smer, krok):
        self.rotace += krok if smer == "R" else (-krok+360)
        if self.rotace < 0: self.rotace = 360 + self.rotace
        if self.rotace >= 360: self.rotace = self.rotace - 360
        if (self.rotace == 0):
            self.pomocna = self.poziceWN
            self.poziceWN = -self.poziceWE
            self.poziceWE = self.pomocna
        elif (self.rotace == 90):
            self.poziceWN = -self.poziceWN
            self.poziceWE = -self.poziceWE
        elif (self.rotace == 180):
            self.poziceWN = -self.poziceWN
            self.poziceWE = -self.poziceWE
        elif (self.rotace == 270):
            self.pomocna = self.poziceWN
            self.poziceWN = -self.poziceWE
            self.poziceWE = self.pomocna

    def pohybW(self, smer, krok):
        if smer == "N":self.poziceWN += krok
        elif smer == "E":self.poziceWE += krok
        elif smer == "S":self.poziceWN -= krok
        elif smer == "W":self.poziceWE -= krok

    def navigace(self, navigacniList):
        for krok in navigacniList:
            print(krok[0], krok[1])
            if krok[0]=="F":
                self.poziceN+=krok[1]*self.poziceWN
                self.poziceE+=krok[1]*self.poziceWE
            elif krok[0] == "L" or krok[0] == "R":
                self.orientace(krok[0], krok[1])
            else: self.pohybW(krok[0],krok[1])

            print(bod.poziceN, bod.poziceE)
            print(bod.poziceWN, bod.poziceWE)


navigacniList=[[line.strip()[0],int(line.strip()[1:])] for line in open("12.txt", "r")]

bod=Waypoint()

"""print(bod.poziceWN, bod.poziceWE, bod.rotaceW)
bod.pohybW("F",10)
print(bod.poziceWN, bod.poziceWE, bod.rotaceW)
print("Pozice waypointu")
bod.pohybW("N",3)
print(bod.poziceWN, bod.poziceWE, bod.rotaceW)
bod.pohybW("F",7)
print(bod.poziceN, bod.poziceE, bod.rotaceW)
print("Pozice lodi")
print(bod.poziceWN, bod.poziceWE, bod.rotaceW)

bod.orientaceW("R",90)
print(bod.poziceWN, bod.poziceWE, bod.rotaceW)
bod.pohybW("F",11)
print(bod.poziceWN, bod.poziceWE, bod.rotaceW)
print("Pozice lodi")"""
bod.navigace(navigacniList)
