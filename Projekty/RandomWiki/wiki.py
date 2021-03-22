import requests
from bs4 import BeautifulSoup
import webbrowser


while True:
    address = requests.get("https://en.wikipedia.org/wiki/Special:Random")  #získá html adresu náhodného článku pomocí odkazu
    html = BeautifulSoup(address.content, 'html.parser')                    #získá html kód článku
    title = html.find(id = "firstHeading").text                             #získá titulek článku
    print(title + "\nChcete tento článek? (Y/N)")
    ans = str(input(""))
    if (ans.lower() == "y"):
        url = 'https://en.wikipedia.org/wiki/%s' %title
        webbrowser.open(url)
        break
    elif (ans.lower() == "n"):
        continue
    else:
        print("Špatná odpověď!")
        break
