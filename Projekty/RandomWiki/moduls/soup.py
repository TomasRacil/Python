import requests
from bs4 import BeautifulSoup
import webbrowser

def soup():
    while True:
        address = requests.get("https://en.wikipedia.org/wiki/Special:Random")      #získá html adresu náhodného článku pomocí odkazu
        html = BeautifulSoup(address.content, 'html.parser')                        #získá html kód článku
        title = html.find(id = "firstHeading").text                                 #získá titulek článku
        odstavec = html.find_all('p')                                               #získá první odstavec v html
        print(title + "\n\n" + odstavec[0].text + "\nChcete tento článek? (Y/N)")   #získá první odstavec textu
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