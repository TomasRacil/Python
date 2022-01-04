import requests, json

url='https://maps.distancematrixapi.com/maps/api/distancematrix/json?'
api_key ='AlphaDMAVhNcGaWYPjbHanGWO0MJyTQqV0HnPVeb'

class Vehicle:
    def __init__(self, avgFuelConsumption, fuelType, fuelCapacity=50):
        self.avgFuelConsumption = avgFuelConsumption
        self.fuelType = fuelType
        self.fuelCapacity=fuelCapacity

    def fuelConsumption(self,distance):
        return distance/100*self.avgFuelConsumption

class Route:
    def __init__(self,vehicles, startLocation, endLocation):

        self.vehicles=vehicles
        self.startLocation = startLocation
        self.endLocation = endLocation

        r=requests.get(url+'origins='+startLocation+'&destinations='+endLocation+'&departure_time=now&key='+api_key).json()
        self.distance = r['rows'][0]['elements'][0]['distance']['value']/1000
    
    def fuelConsumption(self):
        celkovaSpotreba=[0,0]
        for vehicle in self.vehicles:
            if vehicle.fuelType=="benzin":
                celkovaSpotreba[0] += vehicle.fuelConsumption(self.distance)
            elif vehicle.fuelType=="nafta":
                celkovaSpotreba[1] += vehicle.fuelConsumption(self.distance)
        
        return tuple(celkovaSpotreba)


auto1=Vehicle(8,"benzin")
auto2=Vehicle(6,"nafta")
prahaBrno=Route([auto1,auto2],"Praha","Brno")

print(auto1.fuelConsumption(50))
print(auto2.fuelConsumption(50))
print(prahaBrno.distance)
print(prahaBrno.fuelConsumption())
print(prahaBrno.cenaCesty(36,34))
