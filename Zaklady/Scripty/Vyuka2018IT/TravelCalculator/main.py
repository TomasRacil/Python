import requests, json
class Vehicle:
    def __init__(self, avgSpeed, x, avgFuelConsumption,typ, fuelCapacity=50):
        self.avgSpeed=avgSpeed
        self.x=x
        self.avgFuelConsumption = avgFuelConsumption
        self.typ=typ

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
        celkovaSpotrebaNafty=0
        celkovaSpotrebaBenzinu=0
        for vehicle in self.vehicles:
            #celkovaSpotreba+=vehicle.fuelConsumption(self.distance)
            pass
        return (celkovaSpotrebaNafty,celkovaSpotrebaBenzinu)

    def cenaVsech(self,cenaNafty, cenaBenzinu):
        return self.spotrebaVsech()*cenaNafty

prvniAuto=Vehicle(90, 0, 8, 'diesel')
druheAuto=Vehicle(120, 240, 10, 'benzin')

prvniCesta = Route([prvniAuto,druheAuto],0,640, "10:00")
prvniCesta.info()
print(prvniCesta.spotrebaVsech())
print(prvniCesta.cenaVsech(35,35))


api_key ='AlphaDMAVhNcGaWYPjbHanGWO0MJyTQqV0HnPVeb'
  
# Take source as input
source = 'Praha'
  
# Take destination as input
dest = 'Brno'

departure = 'now'
#"https://maps.distancematrixapi.com/maps/api/distancematrix/json?origins=Boston%2CMA%7CCharlestown%2CMA&destinations=Lexington%2CMA%7CConcord%2CMA&departure_time=now&key=AlphaDMAVhNcGaWYPjbHanGWO0MJyTQqV0HnPVeb"
# url variable store url 
url ='https://maps.distancematrixapi.com/maps/api/distancematrix/json?'
  
# Get method of requests module
# return response object
#r=requests.get(url)
r = requests.get(url + 'origins=' + source +
                   '&destinations=' + dest +
                   '&departure_time=' + departure +
                   '&key=' + api_key)
                     
# json method of response object
# return json format result
x = r.json()
  
# by default driving mode considered
  
# print the value of x
print(x)
# dobaCesty=(prvniAuto.x+druheAuto.x)/(prvniAuto.avgSpeed+druheAuto.avgSpeed)
# hodiny=int(dobaCesty)
# minuty=int(60/((dobaCesty-hodiny)*100))
# print(f"delka cesty {hodiny} h a {minuty} m")
# prvniAuto.move(dobaCesty)

# print(prvniAuto.fuelConsumption())

# prvniAuto.info()

