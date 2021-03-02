import json
import requests 

#načtení dat z json struktury
def jsonGetInfo():
    try:
        r = requests.get('https://onemocneni-aktualne.mzcr.cz/api/v1/covid-19/nakazeni-vyleceni-umrti-testy.json/')
    except:
        print("Nelze připojit k serveru")
        r = None
    return json.loads(r.text)
