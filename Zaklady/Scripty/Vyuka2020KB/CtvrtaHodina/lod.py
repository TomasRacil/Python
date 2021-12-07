class Ship:

    def __init__(self,orientation,N,E):
        self.orientation=orientation
        self.N=N
        self.E=E
    
    def info(self):
        return f'Lod směřuje na {self.orientation}, a nachází se na souřadnicích N: {self.N} E: {self.E}'
    
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
        pass


mojeLod=Ship('N',0,0)
mojeLod.changeOrientation('L',90)
mojeLod.changeOrientation('P',90)

print(mojeLod.info())