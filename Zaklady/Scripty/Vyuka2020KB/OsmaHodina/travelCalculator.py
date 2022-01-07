import requests
import xmltodict

url='https://maps.distancematrixapi.com/maps/api/distancematrix/json?'
api_key ='AlphaDMAVhNcGaWYPjbHanGWO0MJyTQqV0HnPVeb'

urlConsumption = "https://www.fueleconomy.gov/ws/rest/ympg/shared/ympgVehicle/"
urlFuelType = "https://www.fueleconomy.gov/ws/rest/vehicle/"
urlCar = "https://www.fueleconomy.gov/ws/rest/vehicle/menu/options?"
urlFuel = "https://www.fueleconomy.gov/ws/rest/fuelprices"
urlRate = "https://cdn.jsdelivr.net/gh/fawazahmed0/currency-api@1/latest/currencies/usd/czk.json"

class Auto:
    def __init__(self):
        id = getID()

        req = requests.get(urlConsumption + id)
        tree = xmltodict.parse(req.content, dict_constructor = dict)['yourMpgVehicle']

        r = requests.get(urlFuelType + id)
        autoInfo = xmltodict.parse(r.content, dict_constructor = dict)['vehicle']

        self.spotreba = round(235.214583 / float(tree['avgMpg']), 2)
        self.druhPaliva = autoInfo['fuelType'].lower()

    def info(self):
        print(f"Průměrná spotřeba auta je {self.spotreba}l/100km a druh paliva je {self.druhPaliva}")

    def vypoctiSpotrebu(self, vzdalenost):
        return vzdalenost * (self.spotreba / 100)

    def getDruhPaliva(self):
        return self.druhPaliva


class Cesta:
    def __init__(self, prvniMisto, druheMisto):
        self.prvniMisto = prvniMisto
        self.druheMisto = druheMisto
        self.listAut = []

        r=requests.get(url + 'origins=' + self.prvniMisto +
                '&destinations=' + self.druheMisto +
                '&departure_time=now'
                '&key=' + api_key)    
        parsed=r.json()

        self.vzdalenost = parsed['rows'][0]['elements'][0]['distance']['value']/1000
    
    def info(self):
        print(f"Vzdálenost z {self.prvniMisto} do {self.druheMisto} je {self.vzdalenost}km")

    def pridejAuto(self, auto):
        self.listAut.append(auto)

    def celkovaSpotreba(self):
        celkovaSpotreba = dict()

        for auto in self.listAut:
            if auto.getDruhPaliva() in celkovaSpotreba:
                celkovaSpotreba[auto.getDruhPaliva()] += auto.vypoctiSpotrebu(self.vzdalenost)
            else:
                celkovaSpotreba[auto.getDruhPaliva()] = auto.vypoctiSpotrebu(self.vzdalenost)

        return celkovaSpotreba

    def cenaCesty(self):
        celkovaSpotreba = self.celkovaSpotreba()

        r = requests.get(urlFuel)
        fuel = xmltodict.parse(r.content, dict_constructor = dict)['fuelPrices']

        req = requests.get(urlRate)
        rate = req.json()

        celkovaCena = 0

        for druhPaliva in celkovaSpotreba:
            celkovaCena += celkovaSpotreba[druhPaliva] * ((float(fuel[druhPaliva]) * float(rate['czk'])) / 3.78541178)

        return celkovaCena
        

def getID():
    rok = input("Rok výroby: ")
    znacka = input("Výrobce: ")
    model = input("Model: ")

    r = requests.get(urlCar + 'year=' + str(rok) +
                    '&make=' + znacka + 
                    '&model=' + model)

    auta = xmltodict.parse(r.content, dict_constructor = dict)['menuItems']['menuItem']

    for id, auto, in enumerate(auta):
        print(f"{id}: {auto['text']}")

    id = int(input("Zadej ID: "))

    return auta[id]['value']


auto1 = Auto() #2012, Honda, Fit, 0 => vybere Regular
auto1.info()

auto2 = Auto() #2014, Honda, Civic, 3 => vybere Premium
auto2.info()

cesta = Cesta("Praha", "Brno")
cesta.info()

cesta.pridejAuto(auto1)
cesta.pridejAuto(auto2)

print(f"Cesta vyjde všechny auta na {round(cesta.cenaCesty(), 2)}Kč")