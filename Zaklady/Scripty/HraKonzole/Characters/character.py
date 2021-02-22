#from Characters import *
class character():
    """třída ze které vychází postavy"""
    type=1 #1=warrior 2=scout 3=mage 4=banditNPC 5=dragonNPC
    hp=100
    damage=100
    energy=100
    lvl=1
    xp=0
    alive=True
    

    def odectiHP(self, kolik):
        if (self.hp-kolik)>0:
            self.hp=self.hp-kolik
        else:
            self.hp=0
            self.alive=False

    def prictiHP(self, kolik):
        self.hp+=kolik

    def odectiEnergy(self, kolik):
        if (self.energy-kolik)>0:
            self.energy=self.energy-kolik
        else:
            self.energy=0

    def ziskejXP(self, kolik):
        self.xp+=kolik

    def ziskejLvl(self, kolik):
        self.lvl+=kolik

    def die(self):
        self.alive=False

    def resurrection(self): #musí se po ní zavolat ještě heal - oživit a uzdravit
        self.alive=True

    def card(self):
        print("====================")
        if self.type==1: print("Typ postavy: Warrior")
        if self.type==2: print("Typ postavy: Scout")
        if self.type==3: print("Typ postavy: Mage")
        if self.type==4: print("Typ postavy: Bandita")
        if self.type==5: print("Typ postavy: Drak")
        print(f"Živý: {self.alive}")
        print(f"Zdraví: {self.hp}")
        print(f"Energie: {self.energy}")
        print(f"Level: {self.lvl}")
        print(f"Zkušenosti: {self.xp}")
        print(f"Dává poškození: {self.damage}\n")
