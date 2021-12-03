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


navigacniList=[[line.strip()[0],int(line.strip()[1:])] for line in open("12.txt", "r")]
"""for line in navigacniList:
    print(line)"""

lod=Ship()
print(lod.poziceN,lod.poziceE,lod.rotace)
lod.navigace(navigacniList)
print(lod.poziceN, lod.poziceE,lod .rotace)


