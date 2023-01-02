from os.path import join, realpath, dirname

class Lod:
    """Trida pro reseni uolu AoC 2020 den 12
    """
    smer = 'E'
    pozice_x = 0
    pozice_y = 0
    
    def __init__(self, navigacniSoubor) -> None:
        self.navigacniData = [(radek.split('\n')[0][0],int(radek.split('\n')[0][1:])) for radek in navigacniSoubor]
        
    def __repr__(self) -> str:
        return f"Poloha lodi x: {self.pozice_x}, y: {self.pozice_y} a smer lodi je {self.smer} vzdalenot manhattan {abs(self.pozice_x)+abs(self.pozice_y)}"
        
    def naviguj(self)->None:
        for prikaz, hodnota in self.navigacniData:
            print(prikaz,":",hodnota)
            if prikaz in ['N','S','E','W','F']:
                self.pohybSmer(prikaz,hodnota)
            elif prikaz in ['R','L']:
                self.otoc(prikaz,hodnota)

    def pohybSmer(self, smer:str, hodnota:int)->None:

        smer = self.smer if smer=='F' else smer

        if smer == 'N':
            self.pozice_y += hodnota
        elif smer == 'S':
            self.pozice_y -= hodnota
        elif smer == 'E':
            self.pozice_x += hodnota
        elif smer == 'W':
            self.pozice_x -= hodnota
    
    def otoc(self, smer: str, hodnota: int)->None:
        smer_na_stupne = {'E':0,'S':90,'W':180,'N':270}
        stupne_na_smer = {0:'E',90:'S',180:'W',270:'N'}
        vychozi_smer = smer_na_stupne[self.smer]
        if smer == 'R':
            novy_smer = vychozi_smer+hodnota
            self.smer = stupne_na_smer[novy_smer%360]
        elif smer == 'L':
            novy_smer = vychozi_smer-hodnota
            self.smer = stupne_na_smer[novy_smer%360]
        
    
soubor = open(join(dirname(realpath(__file__)), "lod.txt"), "r", encoding="utf-8")

lod = Lod(soubor)
print(lod)
lod.naviguj()
# print(lod.__repr__())
print(lod)