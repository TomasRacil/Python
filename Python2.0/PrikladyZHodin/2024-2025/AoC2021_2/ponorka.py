from os import path

class Ponorka:
    # hloubka:int = 0
    def __init__(self, hloubka, vzdalenost):
        self.hloubka:int = hloubka
        self.hloubka2:int = hloubka
        self.vzdalenost: int = vzdalenost
        self.smer = 0
    
    def naviguj(self, radek:str)->None:
        radek = radek.split(' ')
        match (radek[0]):
            case 'up':
                self.hloubka-=int(radek[1])
                self.smer-=int(radek[1])
            case 'down':
                self.hloubka+=int(radek[1])
                self.smer+=int(radek[1])
            case 'forward':
                self.vzdalenost+=int(radek[1])
                self.hloubka2 += int(radek[1])*self.smer
            case _:
                pass
    def vzsledek_1(self):
        print(self.vzdalenost*self.hloubka)
    def vzsledek_2(self):
        print(self.vzdalenost*self.hloubka2)
        

with open(path.join(path.dirname(path.realpath(__file__)), "vstup.txt")) as soubor:
    ponorka = Ponorka(0,0)
    for radek in soubor.readlines():
        ponorka.naviguj(radek)
        # print(ponorka.vzdalenost, ponorka.hloubka2, ponorka.smer)
    ponorka.vzsledek_1()
    ponorka.vzsledek_2()