from os.path import join, realpath, dirname

class Smer:
    x = 10
    y = 1
    
    def __repr__(self) -> str:
        return f"pozice x: {self.x} a pozice y: {self.y}"
    
    def zmen(self, prikaz, hodnota):
        if prikaz in ['R','L']:
            self.otoc(prikaz, hodnota)
        else:
            self.pohyb_smer(prikaz,hodnota)
    
    def pohyb_smer(self, smer, hodnota):
        if smer in ['N','S']:
            self.y = self.y + (hodnota if smer=='N' else -hodnota)
        else:
            self.x = self.x + (hodnota if smer=='E' else -hodnota)
    
    def otoc(self, smer, hodnota):
        if hodnota == 180:
            self.x, self.y = - self.x, - self.y
        elif (smer=='R' and hodnota == 90) or (smer=='L' and hodnota == 270):
            self.x, self.y = self.y, -self.x
        elif (smer=='L' and hodnota == 90) or (smer=='R' and hodnota == 270):
            self.x, self.y = -self.y, self.x

class Lod:
    """Trida pro reseni uolu AoC 2020 den 12
    """
    x = 0
    y = 0
    smer = Smer()
    
    def __init__(self, cesta) -> None:
        with open(cesta,'r',encoding='utf-8') as navigacni_soubor:
            self.navigacniData = [(radek[0],int(radek[1:])) for radek in navigacni_soubor.read().split('\n')]
        
    def __repr__(self) -> str:
        return f"Poloha lodi x: {self.x}, y: {self.y} a smer lodi je {self.smer} vzdalenot manhattan {abs(self.x)+abs(self.y)}"
        
    def naviguj(self)->None:
        for prikaz, hodnota in self.navigacniData:
            if prikaz == 'F':
                self.pohybSmer(hodnota)
            else:
                self.smer.zmen(prikaz,hodnota)

    def pohybSmer(self, hodnota:int)->None:
        self.x += hodnota*self.smer.x
        self.y += hodnota*self.smer.y
        
    
cesta = join(dirname(realpath(__file__)), "lod.txt")
print(cesta)
lod = Lod(cesta)
print(lod)
lod.naviguj()
print(lod)