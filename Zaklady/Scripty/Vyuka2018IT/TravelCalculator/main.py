class Vehicle:
    def __init__(self, avgSpeed, x, avgFuelConsumption, fuelCapacity=50):
        self.avgSpeed=avgSpeed
        self.x=x
        self.avgFuelConsumption = avgFuelConsumption

    def move(self,dobaCesty):
        self.x+=self.avgSpeed*dobaCesty
    def info(self):
        print(f'Auto je na místě {self.x} a má průměrnou rychlost {self.avgSpeed}')

    def fuelConsumption(self,distance):
        return distance/100*self.avgFuelConsumption

class Route:
    def __init__(self,vehicles, startLocation, endLocation,startTime, endTime=None):
        self.vehicles=vehicles
        self.startLocation=startLocation
        self.endLocation = endLocation
        self.startTime = startTime
        self.distance = endLocation-startLocation
    
    def info(self):
        print(f"Cesta z  místa {self.startLocation} do místa {self.endLocation} odjezd {self.startTime} vzdálenost {self.distance}")

    def spotrebaVsech(self):
        celkovaSpotreba=0
        for vehicle in self.vehicles:
            celkovaSpotreba+=vehicle.fuelConsumption(self.distance)
        return celkovaSpotreba

prvniAuto=Vehicle(90, 0, 8)
druheAuto=Vehicle(120, 240, 10)

prvniCesta = Route([prvniAuto,druheAuto],0,640, "10:00")
prvniCesta.info()
print(prvniCesta.spotrebaVsech())


# dobaCesty=(prvniAuto.x+druheAuto.x)/(prvniAuto.avgSpeed+druheAuto.avgSpeed)
# hodiny=int(dobaCesty)
# minuty=int(60/((dobaCesty-hodiny)*100))
# print(f"delka cesty {hodiny} h a {minuty} m")
# prvniAuto.move(dobaCesty)

# print(prvniAuto.fuelConsumption())

# prvniAuto.info()

