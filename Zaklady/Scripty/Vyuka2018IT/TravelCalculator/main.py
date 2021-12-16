import requests, json

url='https://maps.distancematrixapi.com/maps/api/distancematrix/json?'
api_key ='AlphaDMAVhNcGaWYPjbHanGWO0MJyTQqV0HnPVeb'

class Vehicle:
    def __init__(self, avgSpeed, x, avgFuelConsumption,typ, fuelCapacity=50):
        self.avgSpeed=avgSpeed
        self.x=x
        self.avgFuelConsumption = avgFuelConsumption
        self.typ=typ

    def move(self,dobaCesty):
        self.x+=self.avgSpeed*dobaCesty
    def info(self):
        print(f'Auto je na místě {self.x} a má průměrnou rychlost {self.avgSpeed} auto na jednu nadrz uraazi {}')

    def fuelConsumption(self,distance):
        return distance/100*self.avgFuelConsumption

class Route:
    def __init__(self,vehicles, startLocation, endLocation,startTime, endTime=None):

        self.vehicles=vehicles
        self.startLocation = startLocation
        self.endLocation = endLocation
        self.startTime = startTime

        r=requests.get(url + 'origins=' + startLocation +
                   '&destinations=' + endLocation +
                   '&departure_time=now'
                   '&key=' + api_key)    
        parsed=r.json()
        self.distance = parsed['rows'][0]['elements'][0]['distance']['value']/1000
    
    def info(self):
        print(f"Cesta z  místa {self.startLocation} do místa {self.endLocation} odjezd {self.startTime} vzdálenost {self.distance}")

    def spotrebaVsech(self):
        celkovaSpotrebaNafty=0
        celkovaSpotrebaBenzinu=0
        for vehicle in self.vehicles:
            
            if vehicle.typ=='benzin':
                celkovaSpotrebaBenzinu = vehicle.fuelConsumption(self.distance)
            else:
                celkovaSpotrebaNafty = vehicle.fuelConsumption(self.distance)

        return (round(celkovaSpotrebaNafty,2),round(celkovaSpotrebaBenzinu,2))

    def cenaVsech(self,cenaNafty, cenaBenzinu):

        celkem = self.spotrebaVsech()[0] * cenaNafty + self.spotrebaVsech()[1] * cenaBenzinu
        return celkem


#------------------------------------
prvniAuto=Vehicle(90, 0, 8, 'diesel')
druheAuto=Vehicle(120, 240, 10, 'benzin')

prvniCesta = Route([prvniAuto,druheAuto],'Brno','Paris', "10:00")
prvniCesta.info()


print(prvniCesta.spotrebaVsech())
print(prvniCesta.cenaVsech(29,35))


  
# by default driving mode considered
  
# print the value of x
#print("vyd8lenost v metrech: ",x['rows'][0]['elements'][0]['distance']['value'])
# dobaCesty=(prvniAuto.x+druheAuto.x)/(prvniAuto.avgSpeed+druheAuto.avgSpeed)
# hodiny=int(dobaCesty)
# minuty=int(60/((dobaCesty-hodiny)*100))
# print(f"delka cesty {hodiny} h a {minuty} m")
# prvniAuto.move(dobaCesty)

# print(prvniAuto.fuelConsumption())

# prvniAuto.info()

