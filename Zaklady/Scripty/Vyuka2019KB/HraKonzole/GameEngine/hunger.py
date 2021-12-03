from GameEngine import *

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
