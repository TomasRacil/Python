from .character import *

class scout(character):
    def __init__(self,hp=50,energy=150,damage=20):
        self.type=2
        self.hp=hp
        self.energy=energy
        self.damage=damage

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
            print("Upustil jsi lektvar a spadl ti na nohu \nZtrácíš 5 hp.")
              self.hp=hp-5 

        elif hod==2:
                print("Vypadá to že jsi lektavar někde ztratil.")
                
        elif hod==3 or hod==5:
            print("Bylo to vnitřní užití ne?.\nZískáváš 25 hp.")
            self.hp=hp+25

        elif hod==4 or hod==6:
            print("Jsi dokonalý CLS.\nZískáváš 40 hp.")
            self.hp=hp+45