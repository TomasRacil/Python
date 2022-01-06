import requests,json,xmltodict

url='https://maps.distancematrixapi.com/maps/api/distancematrix/json?'
api_key ='AlphaDMAVhNcGaWYPjbHanGWO0MJyTQqV0HnPVeb'

urlConsumption = "https://www.fueleconomy.gov/ws/rest/ympg/shared/ympgVehicle/"
urlCar = "https://www.fueleconomy.gov/ws/rest/vehicle/menu/options?"

class Auto:
    def __init__(self,rok,znacka,model,nadrz,typ_paliva):

        r = requests.get(urlCar + 'year=' + str(rok) +
                        '&make=' + znacka + 
                        '&model=' + model)

        tree = xmltodict.parse(r.content, dict_constructor = dict)['menuItems']['menuItem']

        #vstup uživatele, vybere, který typ daného modelu má ... 0,1,2
        for id, auto, in enumerate(tree):
            print(f"{id}: {auto['text']}")

        hodnota = int(input())   

        req = requests.get(urlConsumption + str(tree[hodnota]['value']))
        tree = xmltodict.parse(req.content, dict_constructor = dict)['yourMpgVehicle']


        self.nadrz = nadrz
        self.typ_paliva = typ_paliva
        self.prum_spotreba = round(235.214583 / float(tree['avgMpg']), 2)
    
    def info(self):
        print(f"Průměrná spotřeba auta je {self.prum_spotreba}l/100km a velikost nádrže je {self.nadrz}l")


    def vypocetSpotreby(self,vzdalenost):
        return vzdalenost* (self.prum_spotreba/100)

    def getTypPaliva(self):
        return self.typ_paliva

class Cesta:
    def __init__(self,start,cil,):
        self.start = start
        self.cil = cil
        self.auta = []

        r=requests.get(url + 'origins=' + start +
                   '&destinations=' + cil +
                   '&departure_time=now'
                   '&key=' + api_key)    
                   
        parsed=r.json()

        self.vzdalenost = parsed['rows'][0]['elements'][0]['distance']['value']/1000

    def info(self):
        print(f"Vzdálenost z {self.start} do {self.cil} je {self.vzdalenost}km")

    def pridejAuto(self,auto):
        self.auta.append(auto)

    def celkovaSpotreba(self):
        celkova_spotreba = [0,0]

        for auto in self.auta:
            if auto.getTypPaliva() == "benzin":
                celkova_spotreba[0] += auto.vypocetSpotreby(self.vzdalenost)
            elif auto.getTypPaliva() == "nafta":
                celkova_spotreba[1] += auto.vypocetSpotreby(self.vzdalenost)

        return celkova_spotreba

    def cenaCesty(self,cena_benzinu,cena_nafty):
        celkova_spotreba = self.celkovaSpotreba()
        return (celkova_spotreba[0] * cena_benzinu) + (celkova_spotreba[1] * cena_nafty)


auto1 = Auto(2012, "Honda", "Fit", 50, "benzin")
auto1.info()

cestaPrahaBrno = Cesta("Praha","Brno")
cestaPrahaBrno.info()

cestaPrahaBrno.pridejAuto(auto1)
#cestaPrahaBrno.pridejAuto(auto2)
#cestaPrahaBrno.pridejAuto(auto3)

print(f"Celková spotřeba benzínových aut na cestě je: {round(cestaPrahaBrno.celkovaSpotreba()[0], 2)}l")
print(f"Celková spotřeba naftových aut na cestě je: {round(cestaPrahaBrno.celkovaSpotreba()[1], 2)}l")

print(f"Cesta vyjde všechny auta na {round(cestaPrahaBrno.cenaCesty(36, 34))}Kč")

