from .character import *

class mage(character):
    def __init__(self,hp=65,energy=100,lvl=1,xp=0,damage=110, hunger=100):
        self.type=3
        self.hp=hp
        self.energy=energy
        self.lvl=lvl
        self.xp=xp
        self.damage=damage
        self.hunger=hunger

    def sleep(self):  
        hod=hodKostkou(1,8)
        print("\nHodil jsi: " + str(hod) + "\n")   

        if hod==1:
            print("Během spánku jsi byl přepaden. \nNezískal jsi žádnou energii")
               

        elif hod==2:
                print("Sotva jsi zamhouřil oči, okolní rámus tvému spánku rozhodně nedopřál!\nZískáváš 30 energie")
                self.energy=30
        elif hod==3:
            print("V průběhu spánku ses několikrát probudil kvůli nočním můrám !\nZískáváš 60 energie")
            self.energy=60

        elif hod==4 or hod==5:
            print("Po několika hodinách se probouzíš, ale spaní na tvrdé podložce nebylo to pravé!\nZískáváš 90 energie")
            self.energy=90

        elif hod==6:
           print("Bylo ti nabídnuto lůžko v blízkém hostinci, takhle dobře ses už dlouho nevyspal!\nZískáváš 120 energie")
           self.energy=120

    def heal(self):  
        hod=hodKostkou(1,8)
        print("\nHodil jsi: " + str(hod) + "\n")   

        if hod==1:
            print("Asi jsi trochu mimo, použil jsi lektvar na špatnou část těla.") 

        elif hod==2:
                print("Vypadá to, že tenhle lektvar je prošlý.\nZískáváš 30 hp.")
                self.hp=hp+30

        elif hod==3 or hod==5:
            print("Tvé léčení bylo úspěšné.\nZískáváš 45 hp.")
            self.hp=hp+45

        elif hod==4 or hod==6:
            print("Tvé léčení by snad oživilo i mrtvého.\nZískáváš 65 hp.")
            self.hp=hp+65

    def train(self):
        hod=hodKostkou(1,6)
        print("\nHodil jsi: " + str(hod) + "\n")   

        if hod == 1:
            print("Promrhal si celý den. Nechtěl jsi náhodou trénovat?\nZískáváš 0 xp.")

        elif hod == 2:
            print("Zkusil sis rychle zacvičit. A stejně rychle tě to přešlo.\nZískáváš 10 xp.")
            self.xp = xp + 10

        elif hod == 3 or hod == 4:
            print("Přečetl jsi půlku manuálu pro dobrodruhy.\nZískáváš 30 xp.")
            self.xp= xp + 30

        elif hod == 5:
            print("Přemluvil jsi náhodného kolemjdoucího na sparring. Snad to ještě někdy rozchodí...\nZískáváš 60 xp.")
            self.xp = xp + 60

        elif hod == 6:
            print("DING!\nZískáváš level.")
            self.lvl = lvl + 1
            
    def hunger(self):
        hod=hodKostkou(1,5)
        print("\nHodil jsi: " + str(hod) + "\n")   

        if hod == 1:
            print("Nenašel jsi žádné jídlo\nZískáváš 0 hunger bodů.")

        elif hod == 2:
            print("Kůrka chleba...najíš se, ale ne moc.\nZískáváš 10 hunger bodů.")
            self.hunger = hunger + 10

        elif hod == 3 or hod == 4:
            print("Celý krajíc chleba a šunka k tomu.\nZískáváš 50 hunger bodů.")
            self.hunger= hunger + 50

        elif hod == 5:
            print("Pečené kuře...konečně jsi najezený\nZískáváš 100 xp.")
            self.hunger = hunger + 100    
