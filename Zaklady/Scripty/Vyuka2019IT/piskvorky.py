class HraciPlocha:
    def __init__(self) -> None:
        self.pole = []
        for _ in range(5):
            radek = []
            for _ in range(5):
                radek.append(" ")
            self.pole.append(radek)
    def __repr__(self) -> str:
        output = ""
        for radek in self.pole: 
            output+="|"+"|".join(radek) + "|\n"
        return output[:-1]
    def get_sloupce(self)->list:
        sloupce=[]
        for idx,_ in enumerate(hra.pole[0]):
            sloupec=''
            for radek in hra.pole:
                sloupec+=radek[idx]
            sloupce.append(sloupec)
        return sloupce
    
    def get_diagonaly(self)->list:
        diagonaly=[]
        diagonalni_body_prava=set()
        diagonalni_body_leva=set()
        for cislo in range(len(self.pole)):
            diagonalni_body_prava.add((cislo,0))
            
        for cislo in range(len(self.pole[0])):
            diagonalni_body_prava.add((0,cislo))
            diagonalni_body_leva.add((0,cislo))

        for cislo in range(len(self.pole[0])):
            diagonalni_body_leva.add((cislo,len(self.pole)-1))
        
        for body in diagonalni_body_prava:
            y,x = body
            diag=""
            while y<len(hra.pole) and x<len(self.pole[0]):
                diag+=hra.pole[y][x]
                x+=1
                y+=1
            diagonaly.append(diag)
        for body in diagonalni_body_leva:
            y,x = body
            diag=""
            while y<len(hra.pole) and x>=0:
                diag+=hra.pole[y][x]
                x-=1
                y+=1
            diagonaly.append(diag)
        return diagonaly
    
    def kontrola_vyhry(self)->bool:
        for radek in self.pole:
            radek = "".join(radek)
            if radek.find("XXXX")!=-1 or radek.find("O"*4)!=-1:
                return True
        
        for sloupec in self.get_sloupce():
            if sloupec.find("XXXX")!=-1 or sloupec.find("OOOO")!=-1:
                return True
        
        for diagonala in self.get_diagonaly():
            if diagonala.find("XXXX")!=-1 or diagonala.find("OOOO")!=-1:
                return True
            
        return False

hra = HraciPlocha()



print(hra)

idx=0
while not hra.kontrola_vyhry():
    hrac1_y = int(input("Hrac 1 zadej y: " if idx%2==0 else "Hrac 2 zadej y: "))
    hrac1_x = int(input("Hrac 1 zadej x: " if idx%2==0 else "Hrac 2 zadej x: "))
    hra.pole[hrac1_y][hrac1_x] = "X" if idx%2==0 else "O"
    print(hra)
    idx+=1

print("Vyhral hrac "+ "2" if idx%2==0 else "1")