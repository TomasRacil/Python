from os.path import realpath, dirname, join

class Lod:
    __sever:int = 0
    __vychod:int = 0
    __stupne:int = 90
    
    def __init__(self, stupne:int, sever:int, vychod:int) -> None:
        self.__sever=sever
        self.__vychod=vychod
        self.__stupne=stupne
    
    def __repr__(self) -> str:
        return f"Severni souradnice je: {self.__sever}\nVychodni souradnice je: {self.__vychod}\nOtoceni lodi je: {self.__stupne}\nVydalenost od pocatku je: {abs(self.__sever)+abs(self.__vychod)}"
    
    def pohyb(self, smer:str, hodnota:int)->None:
        match smer:
            case 'N': self.__sever += hodnota
            case 'S': self.__sever -= hodnota
            case 'E': self.__vychod += hodnota
            case 'W': self.__vychod -= hodnota
            case 'L': self.rotace(smer, hodnota)
            case 'R': self.rotace(smer, hodnota)
            case 'F':
                match self.__stupne:
                    case 0: self.__sever += hodnota
                    case 90: self.__vychod += hodnota
                    case 180: self.__sever -= hodnota
                    case 270: self.__vychod -= hodnota
                    case _: pass
            case _: pass
            
    def rotace(self, smer:str, hodnota:int)->None:
        if (smer == 'L'): self.__stupne -= hodnota
        elif (smer == 'R'): self.__stupne += hodnota;
        if (self.__stupne < 0): self.__stupne += 360;
        elif (self.__stupne >= 360): self.__stupne -= 360
        
    def naviguj(self, soubor:str)->None:
        with open(join(dirname(realpath(__file__)),soubor),"r", encoding="utf_8") as file:
            for line in file.read().split('\n'):
                self.pohyb(line[0],int(line[1:]))
    
    


def main():
    novaLod = Lod(90,0,0)
    novaLod.naviguj("input.txt")
    print(novaLod)
    

# main()
if __name__ == "__main__":
    main()