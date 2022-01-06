import requests
# import json
import xmltodict

url = 'https://maps.distancematrixapi.com/maps/api/distancematrix/json?'
api_key = 'AlphaDMAVhNcGaWYPjbHanGWO0MJyTQqV0HnPVeb'

urlCar = "https://www.fueleconomy.gov/ws/rest/vehicle/menu/options?"
urlCarInfo = "https://www.fueleconomy.gov/ws/rest/vehicle/"
urlPrices = "https://www.fueleconomy.gov/ws/rest/fuelprices"


class Auto:
    def __init__(self, uid, nadrz):

        req = requests.get(urlCarInfo + uid)
        carInfo = xmltodict.parse(req.content, dict_constructor=dict)['vehicle']

        self.nadrz = nadrz
        self.typ_paliva = carInfo['fuelType'].lower()
        self.prum_spotreba = round(235.214583 / float(carInfo['comb08']), 2)

    def info(self):
        s = f"Průměrná spotřeba auta je {self.prum_spotreba}l/100km "\
            f"a velikost nádrže je {self.nadrz}l "\
            f"typ paliva je {self.typ_paliva}"
        print(s)

    def vypocetSpotreby(self, vzdalenost):
        return vzdalenost * (self.prum_spotreba/100)

    def getTypPaliva(self):
        return self.typ_paliva


class Cesta:
    def __init__(self, start, cil, auta):
        self.start = start
        self.cil = cil
        self.auta = auta

        r = requests.get(url + 'origins=' + start +
                         '&destinations=' + cil +
                         '&departure_time=now'
                         '&key=' + api_key)

        parsed = r.json()

        self.vzdalenost = parsed['rows'][0]['elements'][0]['distance']['value']/1000

    def info(self):
        print(
            f"Vzdálenost z {self.start} do {self.cil} je {self.vzdalenost}km")

    def pridejAuto(self, auto):
        self.auta.append(auto)

    def celkovaSpotreba(self):
        celkova_spotreba = dict()

        for auto in self.auta:
            if auto.typ_paliva in celkova_spotreba:
                celkova_spotreba[auto.typ_paliva]+=auto.vypocetSpotreby(self.vzdalenost)
            else:
                celkova_spotreba[auto.typ_paliva]=auto.vypocetSpotreby(self.vzdalenost)

        return celkova_spotreba

    def cenaCesty(self, cena_benzinu, cena_nafty):
        celkova_spotreba = self.celkovaSpotreba()
        return (celkova_spotreba[0] * cena_benzinu) + (celkova_spotreba[1] * cena_nafty)


def getID():
    rok = input("Rok výroby: ")
    znacka = input("Značka: ")
    model = input("Model: ")
    r = requests.get(urlCar + 'year=' + rok +
                     '&make=' + znacka +
                     '&model=' + model)
    auta = xmltodict.parse(r.content, dict_constructor=dict)[
        'menuItems']['menuItem']
    for id, auto, in enumerate(auta):
        print(f"{id}: {auto['text']}")

    id = int(input("Zadej označení modelu: "))

    return auta[id]['value']


r = requests.get(urlPrices)
prices = xmltodict.parse(r.text, dict_constructor=dict)['fuelPrices']
print(prices)

uid = getID()
auto1 = Auto(uid, 50)
auto1.info()
uid = getID()
auto2 = Auto(uid, 50)
auto2.info()

cestaPrahaBrno = Cesta("Praha", "Brno", [auto1,auto2])
cestaPrahaBrno.info()
print(cestaPrahaBrno.celkovaSpotreba())

# cestaPrahaBrno.pridejAuto(auto1)
# cestaPrahaBrno.pridejAuto(auto2)
# cestaPrahaBrno.pridejAuto(auto3)

# print(f"Celková spotřeba benzínových aut na cestě je: {round(cestaPrahaBrno.celkovaSpotreba()[0], 2)}l")
# print(f"Celková spotřeba naftových aut na cestě je: {round(cestaPrahaBrno.celkovaSpotreba()[1], 2)}l")

# print(f"Cesta vyjde všechny auta na {round(cestaPrahaBrno.cenaCesty(36, 34))}Kč")
