class Ship:

    orientation='E'
    N=0
    E=0

    def __init__(self,orientation,N,E):
        self.orientation=orientation
        self.N=N
        self.E=E
    
    def info(self):
        return f'Lod směřuje na {self.orientation}, a nachází se na souřadnicích N: {self.N} E: {self.E} sum= {abs(self.N)+abs(self.E)}'
    
    def changeOrientation(self,direction,value):
        SWEN=['N','E','S','W']
        if direction=='L':
            curIdx=SWEN.index(self.orientation)
            rep=int(value/90)
            self.orientation=SWEN[curIdx-rep]
        else:
            curIdx=SWEN.index(self.orientation)
            rep=int(value/90)
            self.orientation=SWEN[curIdx+rep-4]

    def move(self,direction,value):
        if direction=="F":direction=self.orientation
        if direction=="N":self.N+=value
        elif direction=="S":self.N-=value
        elif direction=="E":self.E+=value
        else:self.E-=value
    
    def navigate(self, navigationData):
        for direction,value in navigationData:
            if direction in ['L','R']:self.changeOrientation(direction,value)
            else:self.move(direction,value)

with open(r"C:\Vyuka\Python\Zaklady\Scripty\Vyuka2020KB\CtvrtaHodina\input.txt","r") as f:
    navigationData=[  (line.strip()[0], int( line.strip()[1:] ) ) for line in f]
    # for line in navigationData:
    #     print(line)



    mojeLod=Ship('E',0,0)
    druhaLod=Ship('N',1,1)
    druhaLod.changeOrientation('P',180)

    # mojeLod.navigate(navigationData)
    print(mojeLod.info())
    print(druhaLod.info())
    # mojeLod.changeOrientation('L',90)
    # mojeLod.changeOrientation('P',90)

    # print(mojeLod.info())