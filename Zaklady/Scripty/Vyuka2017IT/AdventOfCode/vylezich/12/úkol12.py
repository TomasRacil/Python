"""12. úkol - hodina - autroské řešení :("""
class Ship:
    rotace=90
    poziceN=0
    poziceE=0

    def orientace(self,smer, krok):
        self.rotace+=krok if smer=="R" else -krok
        if self.rotace<0: self.rotace=360+self.rotace
        if self.rotace >= 360: self.rotace = self.rotace-360

    def pohyb(self,smer, krok):
        if smer=="N":self.poziceN += krok
        elif smer=="E":self.poziceE += krok
        elif smer=="S":self.poziceN -= krok
        elif smer == "W":self.poziceE -= krok
        elif smer=="F":
            soucasnaRotace=self.rotace
            if soucasnaRotace==0:self.poziceN += krok
            elif soucasnaRotace==90:self.poziceE += krok
            elif soucasnaRotace==180:self.poziceN -= krok
            elif soucasnaRotace == 270:self.poziceE -= krok

    def navigace(self, navigacniList):
        for krok in navigacniList:
            if krok[0]=="L" or krok[0]=="R":
                self.orientace(krok[0],krok[1])
            else: self.pohyb(krok[0],krok[1])

class Waypoint:
    rotaceW=90
    poziceWN = 1
    poziceWE = 10
    rotaceS=90
    poziceS=0
    poziceS=0
    pomocna=0

    def orientaceW(self,smer, krok):
        if smer == "R":
            self.pomocna=self.poziceWE
            self.poziceWE=self.poziceWN
            self.poziceWN = self.pomocna
        elif smer =="L":
            self.rotaceW=0

        if self.rotace < 0: self.rotace = 360 + self.rotace
        if self.rotace >= 360: self.rotace = self.rotace - 360

    def pohybW(self, smer, krok):
        if smer == "N":self.poziceWN += krok
        elif smer == "E":self.poziceWE += krok
        elif smer == "S":self.poziceWN -= krok
        elif smer == "W":self.poziceWE -= krok
        elif smer == "F":
            soucasnaRotace = self.rotaceW
            if soucasnaRotace == 0:
                self.poziceS += krok
            elif soucasnaRotace == 90:
                self.poziceS += krok
            elif soucasnaRotace == 180:
                self.poziceS -= krok
            elif soucasnaRotace == 270:self.poziceWE -= krok

    def navigace(self, navigacniList):
        for krok in navigacniList:
            if krok[0]=="L" or krok[0]=="R":
                self.orientace(krok[0],krok[1])
            else: self.pohyb(krok[0],krok[1])


navigacniList=[[line.strip()[0],int(line.strip()[1:])] for line in open("12.txt", "r")]
for line in navigacniList:
    print(line)

lod=Ship()
bod=Waypoint()
"""print(lod.poziceN,lod.poziceE,lod.rotace)
lod.navigace(navigacniList)
print(lod.poziceN, lod.poziceE,lod .rotace)"""

"""print(lod.poziceN, lod.poziceE, lod.rotace)
lod.pohyb("F",10)
print(lod.poziceN, lod.poziceE, lod.rotace)
lod.pohyb("N",3)
print(lod.poziceN, lod.poziceE, lod.rotace)
lod.pohyb("F",7)
print(lod.poziceN, lod.poziceE, lod.rotace)
lod.orientace("R",90)
print(lod.poziceN, lod.poziceE, lod.rotace)
lod.pohyb("F",11)
print(lod.poziceN, lod.poziceE, lod.rotace)"""

print(bod.poziceWN, bod.poziceWE, bod.rotaceW)
bod.pohybW("F",10)
print(bod.poziceWN, bod.poziceWE, bod.rotaceW)
bod.pohybW("N",3)
print(bod.poziceWN, bod.poziceWE, bod.rotaceW)
bod.pohybW("F",7)
print(bod.poziceWN, bod.poziceWE, bod.rotaceW)
bod.orientaceW("R",90)
print(bod.poziceWN, bod.poziceWE, bod.rotaceW)
bod.pohybW("F",11)
print(bod.poziceWN, bod.poziceWE, bod.rotaceW)