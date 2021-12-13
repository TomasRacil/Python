class Vehicle:
    def __init__(self, avgSpeed, x, avgFuelConsumption, fuelCapacity=50):
        self.avgSpeed=avgSpeed
        self.x=x
        self.avgFuelConsumption = avgFuelConsumption

    def move(self,dobaCesty):
        self.x+=self.avgSpeed*dobaCesty
    def info(self):
        print(f'Auto je na místě {self.x} a má průměrnou rychlost {self.avgSpeed}')

    def fuelConsumption(self):
        pass

class Route:
    def __init__(self,cars,distance,start):
        pass

prvniAuto=Vehicle(90, 0, 8)
druheAuto=Vehicle(120, 240, 8)

dobaCesty=(prvniAuto.x+druheAuto.x)/(prvniAuto.avgSpeed+druheAuto.avgSpeed)
hodiny=int(dobaCesty)
minuty=int(60/((dobaCesty-hodiny)*100))
print(f"delka cesty {hodiny} h a {minuty} m")
prvniAuto.move(dobaCesty)

prvniAuto.info()

